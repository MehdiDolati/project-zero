$ErrorActionPreference = "Stop"

Write-Host "Configuring Project Zero Git hooks..."

git config core.hooksPath .githooks

$hooksPath = git config --get core.hooksPath

if ($hooksPath -ne ".githooks") {
    Write-Error "Failed to configure Git hooks."
    exit 1
}

Write-Host ""
Write-Host "Project Zero Git hooks configured successfully."
Write-Host "Hooks path: $hooksPath"