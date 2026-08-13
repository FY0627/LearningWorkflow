<#
.SYNOPSIS
    Frank Agentic Skill Package 安装/部署脚本
#>

param (
    [string]$DestinationRoot = "$HOME\.gemini\config\skills",
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$AgentsRoot = Split-Path -Parent $ScriptDir
$SourceSkillsDir = Join-Path $AgentsRoot "skills"

if (-not (Test-Path $SourceSkillsDir)) {
    Write-Error "找不到 skills 源码目录: $SourceSkillsDir"
}

Write-Host "🚀 开始安装 Frank Agentic Skill Package..." -ForegroundColor Green
Write-Host "📍 目标目录: $DestinationRoot" -ForegroundColor Cyan

if (-not (Test-Path $DestinationRoot)) {
    New-Item -ItemType Directory -Path $DestinationRoot -Force | Out-Null
}

$skills = Get-ChildItem -Path $SourceSkillsDir -Directory
foreach ($skill in $skills) {
    $targetDir = Join-Path $DestinationRoot $skill.Name
    if ((Test-Path $targetDir) -and (-not $Force)) {
        Write-Host "  [跳过] $($skill.Name) 已存在。使用 -Force 参数覆盖安装。" -ForegroundColor Yellow
        continue
    }
    
    Copy-Item -Path $skill.FullName -Destination $DestinationRoot -Recurse -Force
    Write-Host "  [安装] $($skill.Name) -> $targetDir" -ForegroundColor Green
}

Write-Host "✅ 安装完成！" -ForegroundColor Green
