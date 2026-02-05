# Push Bachelorprosjekt til GitHub (kasa031/Bacheloroppgave)
# Kjør fra prosjektmappen, f.eks. hoyreklikk og "Kjor med PowerShell"

Set-Location $PSScriptRoot

# Forsok a legge Git i PATH for denne sessionen hvis git ikke finnes
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    $gitPaths = @("C:\Program Files\Git\cmd", "C:\Program Files (x86)\Git\cmd", "$env:LOCALAPPDATA\Programs\Git\cmd")
    foreach ($p in $gitPaths) {
        if (Test-Path $p) { $env:Path = "$p;$env:Path"; break }
    }
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Git finnes ikke i PATH. Kjor først: .\legg-git-i-path.ps1" -ForegroundColor Red
    Write-Host "Eller installer Git fra https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

if (-not (Test-Path .git)) {
    git init
    git add .
    git commit -m "Forste versjon: cybersikkerhetsnettside"
}
else {
    git add .
    git status
    git commit -m "Oppdatering" -ErrorAction SilentlyContinue
}

git remote remove origin -ErrorAction SilentlyContinue
git remote add origin https://github.com/kasa031/Bacheloroppgave.git
git branch -M main
git push -u origin main

Write-Host "Ferdig. Sjekk https://github.com/kasa031/Bacheloroppgave" -ForegroundColor Green
