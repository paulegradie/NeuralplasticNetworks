$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
& (Join-Path $ScriptDir "start_exp13_2_run.ps1") -Profile "smoke" -ProgressEvery 1
