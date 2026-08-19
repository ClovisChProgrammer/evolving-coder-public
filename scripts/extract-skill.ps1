#!/usr/bin/env pwsh
# Skill Extraction Helper
# Creates a new skill from a learning entry
# Usage: ./extract-skill.ps1 <skill-name> [-DryRun] [-OutputDir <path>]

param(
    [Parameter(Position=0, Mandatory=$false)]
    [string]$SkillName,

    [Parameter()]
    [switch]$DryRun,

    [Parameter()]
    [string]$OutputDir = "./skills",

    [Parameter()]
    [switch]$Help
)

function Show-Help {
    @"
Usage: extract-skill.ps1 <skill-name> [options]

Create a new skill from a learning entry.

Arguments:
  skill-name     Name of the skill (lowercase, hyphens for spaces)

Options:
  -DryRun        Show what would be created without creating files
  -OutputDir     Relative output directory (default: ./skills)
  -Help          Show this help message

Examples:
  .\extract-skill.ps1 docker-m1-fixes
  .\extract-skill.ps1 api-timeout-patterns -DryRun
  .\extract-skill.ps1 pnpm-setup -OutputDir ./skills/custom

The skill will be created in: <OutputDir>/<skill-name>/
"@
}

if ($Help -or !$SkillName) {
    Show-Help
    exit
}

# Validate skill name format
if ($SkillName -notmatch '^[a-z0-9]+(-[a-z0-9]+)*$') {
    Write-Error "Invalid skill name format. Use lowercase letters, numbers, and hyphens only."
    Write-Error "Examples: 'docker-fixes', 'api-patterns', 'pnpm-setup'"
    exit 1
}

# Normalize output path
$OutputDir = $OutputDir.TrimEnd('/').TrimEnd('\')
$SkillPath = Join-Path $OutputDir $SkillName

# Check if skill already exists
if (Test-Path $SkillPath -PathType Container) {
    Write-Error "Skill already exists: $SkillPath"
    Write-Error "Use a different name or remove the existing skill first."
    exit 1
}

# Generate Title Case name from kebab-case
$TitleName = ($SkillName -split '-' | ForEach-Object { "$(Get-Culture).TextInfo.ToTitleCase($_)" }) -join ' '

$Template = @"
---
name: $SkillName
description: "[TODO: Add a concise description of what this skill does and when to use it]"
---

# $TitleName

[TODO: Brief introduction explaining the skill's purpose]

## Quick Reference

| Situation | Action |
|-----------|--------|
| [Trigger condition] | [What to do] |

## Usage

[TODO: Detailed usage instructions]

## Examples

[TODO: Add concrete examples]

## Source Learning

This skill was extracted from a learning entry.
- Learning ID: [TODO: Add original learning ID]
- Original File: .learnings/LEARNINGS.md
"@

if ($DryRun) {
    Write-Host "[INFO] Dry run - would create:" -ForegroundColor Green
    Write-Host "  $SkillPath/"
    Write-Host "  $SkillPath/SKILL.md"
    Write-Host ""
    Write-Host "Template content would be:"
    Write-Host "---"
    Write-Host $Template
    Write-Host "---"
} else {
    Write-Host "[INFO] Creating skill: $SkillName" -ForegroundColor Green

    New-Item -ItemType Directory -Path $SkillPath -Force | Out-Null

    $SkillFile = Join-Path $SkillPath "SKILL.md"
    Set-Content -Path $SkillFile -Value $Template -Encoding utf8

    Write-Host "[INFO] Created: $SkillFile" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:"
    Write-Host "  1. Edit $SkillFile"
    Write-Host "  2. Fill in the TODO sections with content from your learning"
    Write-Host "  3. Add references/ folder if you have detailed documentation"
    Write-Host "  4. Add scripts/ folder if you have executable code"
    Write-Host "  5. Update the original learning entry with:"
    Write-Host "     **Status**: promoted_to_skill"
    Write-Host "     **Skill-Path**: skills/$SkillName"
}
