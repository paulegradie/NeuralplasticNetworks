$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host "Experiment 15: neural baseline comparator full profile" -ForegroundColor Cyan
Write-Host "Directory: $ScriptDir" -ForegroundColor DarkCyan
Write-Host "This full profile trains multiple small neural models across seeds, route lengths, and world counts." -ForegroundColor Yellow

$CandidatePythons = @(
    (Join-Path $ScriptDir "..\..\.venv\Scripts\python.exe"),
    (Join-Path $ScriptDir "..\.venv\Scripts\python.exe"),
    (Join-Path $ScriptDir ".venv\Scripts\python.exe")
)

$Python = $null
foreach ($Candidate in $CandidatePythons) {
    if (Test-Path $Candidate) {
        $Python = $Candidate
        break
    }
}

if (-not $Python) {
    $Python = "python"
}

Write-Host "Using Python: $Python" -ForegroundColor DarkCyan
Write-Host "Starting full-profile run..." -ForegroundColor Yellow
& $Python "run_experiment15.py" "--profile" "full"
if ($LASTEXITCODE -ne 0) {
    throw "Experiment 15 full-profile run failed with exit code $LASTEXITCODE"
}

Write-Host "Analyzing latest Exp15 run..." -ForegroundColor Yellow
& $Python "analyze_experiment15.py" "--analysis-root" "analysis"
if ($LASTEXITCODE -ne 0) {
    throw "Experiment 15 analysis failed with exit code $LASTEXITCODE"
}

Write-Host "Validating latest Exp15 artifacts..." -ForegroundColor Yellow
& $Python "validate_experiment15.py" "--analysis-root" "analysis"
if ($LASTEXITCODE -ne 0) {
    throw "Experiment 15 artifact validation failed with exit code $LASTEXITCODE"
}

Write-Host "Experiment 15 full profile complete." -ForegroundColor Green
Write-Host "Upload the latest analysis/exp15_full_* directory for analysis and manuscript integration." -ForegroundColor Green
