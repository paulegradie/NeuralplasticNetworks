#!/usr/bin/env python3
"""Analyze Experiment 15 neural baseline comparator outputs."""
from __future__ import annotations

import argparse, json, math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REQUIRED_METRICS = ("transition_accuracy", "seen_route_composition_accuracy", "suffix_route_composition_accuracy", "first_step_context_conflict_accuracy", "retention_after_sequential_worlds")
PLOTS = {
    "seen_vs_suffix": "exp15_seen_vs_suffix_composition.png",
    "context_conflict": "exp15_context_conflict_accuracy.png",
    "retention": "exp15_retention_after_sequential_worlds.png",
    "route_length": "exp15_route_length_scaling.png",
    "world_count": "exp15_world_count_scaling.png",
}

def latest(root: Path) -> Path:
    runs=sorted([p for p in root.glob("exp15_*") if p.is_dir()], key=lambda p:p.stat().st_mtime, reverse=True)
    if not runs: raise FileNotFoundError(f"No exp15_* directories under {root}")
    return runs[0]

def ci95(values):
    vals=[float(v) for v in values if math.isfinite(float(v))]
    if len(vals)<=1: return 0.0
    return 1.96*float(np.std(vals,ddof=1))/math.sqrt(len(vals))

def cohen_d(a,b):
    a=np.array([float(x) for x in a if math.isfinite(float(x))]); b=np.array([float(x) for x in b if math.isfinite(float(x))])
    if len(a)<2 or len(b)<2: return float("nan")
    pooled=math.sqrt(((len(a)-1)*float(np.var(a,ddof=1))+(len(b)-1)*float(np.var(b,ddof=1)))/(len(a)+len(b)-2))
    return 0.0 if pooled==0 and float(np.mean(a))==float(np.mean(b)) else ((float(np.mean(a))-float(np.mean(b)))/pooled if pooled else float("inf"))

def summarize(df: pd.DataFrame) -> pd.DataFrame:
    cols=["profile","variant","variant_family","model_kind","training_regime","context_available","replay_enabled","parameter_isolated","world_count","route_length","metric_name","probe_type"]
    rows=[]
    for key,g in df.groupby(cols, dropna=False):
        vals=pd.to_numeric(g["metric_value"],errors="coerce").dropna().astype(float); row=dict(zip(cols,key))
        row.update({"mean":float(vals.mean()) if len(vals) else float("nan"),"sd":float(vals.std(ddof=1)) if len(vals)>1 else 0.0,"sem":float(vals.sem(ddof=1)) if len(vals)>1 else 0.0,"ci95":ci95(vals.tolist()),"min":float(vals.min()) if len(vals) else float("nan"),"max":float(vals.max()) if len(vals) else float("nan"),"n_seed_metric_rows":int(len(vals)),"n_seeds":int(g["seed"].nunique()),"n_eval_total":int(pd.to_numeric(g["n_eval"],errors="coerce").fillna(0).sum())})
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["metric_name","world_count","route_length","variant"]).reset_index(drop=True)

def effect_sizes(df: pd.DataFrame) -> pd.DataFrame:
    anchors={"transition_mlp":"neural_transition_mlp_context","gru_rollout":"neural_gru_rollout_context","gru_endpoint":"neural_gru_endpoint_context"}; rows=[]
    for (wc,rl,metric), g in df.groupby(["world_count","route_length","metric_name"]):
        for label, anchor in anchors.items():
            av=g.loc[g["variant"]==anchor,"metric_value"].astype(float).tolist()
            if not av: continue
            for variant, vg in g.groupby("variant"):
                if variant==anchor: continue
                vv=vg["metric_value"].astype(float).tolist()
                rows.append({"anchor_label":label,"anchor_variant":anchor,"comparison_variant":variant,"world_count":wc,"route_length":rl,"metric_name":metric,"anchor_mean":float(np.mean(av)),"comparison_mean":float(np.mean(vv)),"mean_difference_comparison_minus_anchor":float(np.mean(vv)-np.mean(av)),"cohen_d_comparison_minus_anchor":cohen_d(vv,av),"n_anchor":len(av),"n_comparison":len(vv)})
    return pd.DataFrame(rows)

def label(v: str) -> str:
    return v.replace("neural_","").replace("transition_mlp","mlp").replace("_context","+ctx").replace("_no_context","-ctx").replace("_","\n")

def plot_seen_suffix(summary: pd.DataFrame, out: Path):
    d=summary[summary["metric_name"].isin(["seen_route_composition_accuracy","suffix_route_composition_accuracy"])].copy()
    if d.empty: return
    wc=int(d["world_count"].max()); rl=int(d["route_length"].max()); d=d[(d["world_count"]==wc)&(d["route_length"]==rl)]
    p=d.pivot_table(index="variant",columns="metric_name",values="mean",aggfunc="mean").fillna(0).sort_index(); x=np.arange(len(p)); w=.38
    fig,ax=plt.subplots(figsize=(max(10,len(p)*.9),6)); ax.bar(x-w/2,p.get("seen_route_composition_accuracy",pd.Series(0,index=p.index)),w,label="seen"); ax.bar(x+w/2,p.get("suffix_route_composition_accuracy",pd.Series(0,index=p.index)),w,label="suffix"); ax.set_ylim(0,1.05); ax.set_ylabel("accuracy"); ax.set_title(f"Exp15 seen vs suffix composition, world_count={wc}, route_length={rl}"); ax.set_xticks(x); ax.set_xticklabels([label(v) for v in p.index],rotation=45,ha="right"); ax.legend(); fig.tight_layout(); fig.savefig(out/PLOTS["seen_vs_suffix"],dpi=160); plt.close(fig)

def plot_bar(summary, metric, title, filename, out):
    d=summary[summary["metric_name"]==metric].copy()
    if d.empty: return
    wc=int(d["world_count"].max()); rl=int(d["route_length"].max()); d=d[(d["world_count"]==wc)&(d["route_length"]==rl)].sort_values("variant"); x=np.arange(len(d))
    fig,ax=plt.subplots(figsize=(max(10,len(d)*.9),6)); ax.bar(x,d["mean"].astype(float)); ax.errorbar(x,d["mean"].astype(float),yerr=d["ci95"].astype(float),fmt="none",capsize=3); ax.set_ylim(0,1.05); ax.set_ylabel("accuracy"); ax.set_title(f"{title}, world_count={wc}, route_length={rl}"); ax.set_xticks(x); ax.set_xticklabels([label(v) for v in d["variant"]],rotation=45,ha="right"); fig.tight_layout(); fig.savefig(out/filename,dpi=160); plt.close(fig)

def plot_scaling(summary, xcol, metric, filename, out):
    d=summary[summary["metric_name"]==metric].copy()
    if d.empty: return
    if xcol=="route_length": d=d[d["world_count"]==d["world_count"].max()]; title=f"Exp15 route-length scaling at world_count={int(d['world_count'].max())}"; xlabel="route length"
    else: d=d[d["route_length"]==d["route_length"].max()]; title=f"Exp15 world-count scaling at route_length={int(d['route_length'].max())}"; xlabel="world count"
    fig,ax=plt.subplots(figsize=(10,6))
    for variant,g in d.groupby("variant"):
        g=g.sort_values(xcol); ax.plot(g[xcol].astype(float),g["mean"].astype(float),marker="o",label=variant)
    ax.set_ylim(0,1.05); ax.set_xlabel(xlabel); ax.set_ylabel(metric); ax.set_title(title); ax.legend(fontsize=7); fig.tight_layout(); fig.savefig(out/filename,dpi=160); plt.close(fig)

def report(run_dir: Path, manifest: Dict[str,Any], summary: pd.DataFrame, runtime: pd.DataFrame):
    wc=int(summary["world_count"].max()) if not summary.empty else None; rl=int(summary["route_length"].max()) if not summary.empty else None
    hard=summary[(summary["world_count"]==wc)&(summary["route_length"]==rl)] if wc is not None else summary
    selected=hard[hard["metric_name"].isin(REQUIRED_METRICS)][["variant","metric_name","mean","ci95","n_seeds"]].sort_values(["variant","metric_name"])
    rt=runtime.groupby("variant",as_index=False)["runtime_seconds"].mean().sort_values("runtime_seconds",ascending=False) if not runtime.empty else pd.DataFrame()
    lines=["# Experiment 15 Analysis Report","",f"Generated: {datetime.now(timezone.utc).isoformat()}",f"Run ID: `{manifest.get('run_id',run_dir.name)}`",f"Profile: `{manifest.get('profile','unknown')}`","","## Purpose","","Experiment 15 compares small neural sequence baselines against transition, seen-route, suffix-route, context-conflict, retention, and runtime probes.","","## Hardest-slice metric summary","",f"Hardest summarized slice: `world_count={wc}`, `route_length={rl}`.","", selected.to_markdown(index=False) if not selected.empty else "No selected metrics available.","","## Runtime summary","", rt.to_markdown(index=False) if not rt.empty else "No runtime rows available.","","## Interpretation guardrails","","- Do not treat Exp15 as an exhaustive architecture search.","- Endpoint models and transition/rollout models answer different questions.","- No-context failures are meaningful because the generator creates incompatible world-specific successors.","- Replay and parameter isolation are conventional neural controls, not biological claims.",""]
    text="\n".join(lines); (run_dir/"exp15_report.md").write_text(text,encoding="utf-8"); (run_dir/"experiment_report.md").write_text(text,encoding="utf-8")

def analyze(run_dir: Path):
    metrics=pd.read_csv(run_dir/"exp15_seed_metrics.csv"); runtime=pd.read_csv(run_dir/"exp15_model_runtime.csv"); manifest=json.loads((run_dir/"run_manifest.json").read_text(encoding="utf-8"))
    summary=summarize(metrics); effects=effect_sizes(metrics); summary.to_csv(run_dir/"exp15_summary.csv",index=False); effects.to_csv(run_dir/"exp15_effect_sizes.csv",index=False)
    plots=run_dir/"plots"; plots.mkdir(exist_ok=True); plot_seen_suffix(summary,plots); plot_bar(summary,"first_step_context_conflict_accuracy","Exp15 first-step context conflict accuracy",PLOTS["context_conflict"],plots); plot_bar(summary,"retention_after_sequential_worlds","Exp15 retention after sequential worlds",PLOTS["retention"],plots); plot_scaling(summary,"route_length","suffix_route_composition_accuracy",PLOTS["route_length"],plots); plot_scaling(summary,"world_count","suffix_route_composition_accuracy",PLOTS["world_count"],plots); report(run_dir,manifest,summary,runtime); print(f"Exp15 analysis complete: {run_dir}")

def parse_args(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("--analysis-root",default="analysis"); p.add_argument("--run-dir",default=None); return p.parse_args(argv)

def main(argv=None):
    a=parse_args(argv); analyze(Path(a.run_dir) if a.run_dir else latest(Path(a.analysis_root))); return 0
if __name__=="__main__": raise SystemExit(main())
