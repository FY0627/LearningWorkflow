<#
.SYNOPSIS
    Install the skill pack into one or more agent skill directories.

.DESCRIPTION
    Copies every directory under skills/ that contains a SKILL.md into the skill
    directory of the selected agent(s). Existing skills are never overwritten
    silently: the script throws unless -Force is supplied.

.PARAMETER Target
    Which agent(s) to install for: claude, codex, gemini, or all. Defaults to claude.

.PARAMETER DestinationRoot
    Install to an explicit path instead of the well-known location for -Target.

.PARAMETER Force
    Overwrite skills that already exist at the destination.

.EXAMPLE
    ./scripts/install.ps1 -Target all -WhatIf
    Show what would be installed for every agent without writing anything.

.EXAMPLE
    ./scripts/install.ps1 -Target claude -Force
    Reinstall into ~/.claude/skills, replacing existing copies.
#>

[CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'Medium')]
param(
    [ValidateSet('claude', 'codex', 'gemini', 'all')]
    [string[]]$Target = @('claude'),

    [string]$DestinationRoot,

    [switch]$Force
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSCommandPath)
$SourceSkillsDir = Join-Path $RepoRoot 'skills'

if (-not (Test-Path -LiteralPath $SourceSkillsDir)) {
    throw "Source skills directory not found: $SourceSkillsDir"
}

$KnownRoots = [ordered]@{
    claude = Join-Path $HOME '.claude/skills'
    codex  = Join-Path $HOME '.codex/skills'
    gemini = Join-Path $HOME '.gemini/config/skills'
}

if ($DestinationRoot) {
    $destinations = [ordered]@{ custom = $DestinationRoot }
}
elseif ($Target -contains 'all') {
    $destinations = $KnownRoots
}
else {
    $destinations = [ordered]@{}
    foreach ($name in $Target) { $destinations[$name] = $KnownRoots[$name] }
}

# Only directories carrying a SKILL.md are installable skills. This deliberately
# excludes templates and any scratch directory that ends up under skills/.
$skills = Get-ChildItem -LiteralPath $SourceSkillsDir -Directory |
    Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') } |
    Sort-Object Name

if ($skills.Count -eq 0) {
    throw "No installable skills found under $SourceSkillsDir (a skill needs a SKILL.md)."
}

Write-Host "Source: $SourceSkillsDir ($($skills.Count) skills)"

$installed = 0
$skipped = 0

foreach ($entry in $destinations.GetEnumerator()) {
    $agent = $entry.Key
    $root = $entry.Value

    Write-Host ""
    Write-Host "Target [$agent] -> $root"

    if (-not (Test-Path -LiteralPath $root)) {
        if ($PSCmdlet.ShouldProcess($root, 'Create skills directory')) {
            New-Item -ItemType Directory -Path $root -Force | Out-Null
        }
    }

    foreach ($skill in $skills) {
        $targetDir = Join-Path $root $skill.Name

        if ((Test-Path -LiteralPath $targetDir) -and (-not $Force)) {
            throw "Refusing to overwrite existing skill: $targetDir`nRe-run with -Force to replace it."
        }

        if ($PSCmdlet.ShouldProcess($targetDir, 'Install skill')) {
            if (Test-Path -LiteralPath $targetDir) {
                Remove-Item -LiteralPath $targetDir -Recurse -Force
            }
            Copy-Item -LiteralPath $skill.FullName -Destination $root -Recurse -Force
            Write-Host "  installed  $($skill.Name)"
            $installed++
        }
        else {
            Write-Host "  would install  $($skill.Name) -> $targetDir"
            $skipped++
        }
    }
}

Write-Host ""
if ($WhatIfPreference) {
    Write-Host "Dry run complete: $skipped skill installation(s) would be performed."
}
else {
    Write-Host "Done: $installed skill(s) installed."
    Write-Host ""
    Write-Host "Copying files does not make a gate run. A skill loads only when the host judges"
    Write-Host "its description a match, and that judgement happens before any rule inside the"
    Write-Host "skill can apply. Any skill that must not be skipped also needs a line in the"
    Write-Host "consuming project's CLAUDE.md or AGENTS.md making the call part of the workflow."
    Write-Host "See README.md, 'Installing a gate is not enough'."
}
