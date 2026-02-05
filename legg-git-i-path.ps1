# Legger Git i PATH sa du kan bruke 'git' i PowerShell
# Hoyreklikk -> Kjor med PowerShell (evt. kjor som administrator for permanent PATH)

$gitPaths = @(
    "C:\Program Files\Git\cmd",
    "C:\Program Files (x86)\Git\cmd",
    "$env:LOCALAPPDATA\Programs\Git\cmd"
)

$gitFound = $null
foreach ($p in $gitPaths) {
    if (Test-Path $p) {
        $gitFound = $p
        break
    }
}

if ($gitFound) {
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($currentPath -notlike "*$gitFound*") {
        [Environment]::SetEnvironmentVariable("Path", "$gitFound;$currentPath", "User")
        Write-Host "Git lagt til i PATH (bruker): $gitFound" -ForegroundColor Green
        Write-Host "Lukk og apne terminalen pa nytt, sa fungerer 'git'." -ForegroundColor Yellow
    }
    else {
        Write-Host "Git er allerede i PATH: $gitFound" -ForegroundColor Green
    }
    # Legg til i denne sessionen sa du kan bruke git na
    $env:Path = "$gitFound;$env:Path"
    Write-Host "Git er tilgjengelig i denne sessionen. Proov: git --version" -ForegroundColor Cyan
}
else {
    Write-Host "Git ble ikke funnet. Installer Git fra: https://git-scm.com/download/win" -ForegroundColor Red
    Write-Host "Sjekkte: $($gitPaths -join ', ')" -ForegroundColor Gray
}
