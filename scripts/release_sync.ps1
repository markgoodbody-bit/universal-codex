param(
    [Parameter(Mandatory = $true)]
    [string]$Version
)

$ErrorActionPreference = "Stop"

Write-Host "=== Universal Codex release helper ==="
Write-Host "Version: $Version"
Write-Host ""

# Ensure we're in repo root
if (-not (Test-Path ".git")) {
    Write-Error "This script must be run from the root of the universal-codex repo."
    exit 1
}

# Verify codex/v<Version> exists (envelope versions live here: v1.1.2, etc.)
$codexVersionPath = "codex\v$Version"
if (-not (Test-Path $codexVersionPath)) {
    Write-Error "Expected directory '$codexVersionPath' not found. Check the -Version argument."
    exit 1
}

# Warn if lattice/specs missing – but do not fail
if (-not (Test-Path "lattice")) {
    Write-Warning "lattice/ not found – Lattice layer will not be packaged."
}
if (-not (Test-Path "specs")) {
    Write-Warning "specs/ not found – TT2/spec docs will not be packaged."
}

# Prepare dist/
$dist = "dist"
if (-not (Test-Path $dist)) {
    New-Item -ItemType Directory -Path $dist | Out-Null
}

# Clear old zips
Get-ChildItem $dist -Filter "UniversalCodex*.zip" -ErrorAction SilentlyContinue |
    Remove-Item -Force -ErrorAction SilentlyContinue

# Build versioned zip
$pathsForVersion = @(
    $codexVersionPath,
    "docs",
    "LICENSE",
    "README.md",
    "VERSION"
)
if (Test-Path "lattice") { $pathsForVersion += "lattice" }
if (Test-Path "specs")  { $pathsForVersion += "specs"  }

$versionZip = Join-Path $dist ("UniversalCodex_{0}.zip" -f $Version)
Write-Host "Packing $versionZip ..."
Compress-Archive -Path $pathsForVersion -DestinationPath $versionZip -Force

# Build latest zip (uses codex/latest plus same overlays)
$pathsForLatest = @(
    "codex\latest",
    "docs",
    "LICENSE",
    "README.md",
    "VERSION"
)
if (Test-Path "lattice") { $pathsForLatest += "lattice" }
if (Test-Path "specs")  { $pathsForLatest += "specs"  }

$latestZip = Join-Path $dist "UniversalCodex_latest.zip"
Write-Host "Packing $latestZip ..."
Compress-Archive -Path $pathsForLatest -DestinationPath $latestZip -Force

Write-Host ""
Write-Host "Built zips in .\dist:"
Get-ChildItem $dist

Write-Host ""
Write-Host "Note: This script only builds the zips. Uploading to GitHub releases is still manual."
Write-Host "Done."
