<#
.SYNOPSIS
    KAI Health Check
.DESCRIPTION
    Verifica integridade do sistema no startup.
    Saida: secoes CRITICAL / WARNING / INFO
.NOTES
    Versao: 1.0
    Execucao: startup de toda sessao (integrado ao AGENTS.md)
#>

$repoPath = "$PSScriptRoot\.."
Push-Location $repoPath

$critical = @()
$warning = @()
$info = @()

# CRITICAL

$dirty = git status --porcelain 2>$null
if ($dirty) {
    $critical += "Working directory has uncommitted changes."
}

$gitignore = Get-Content ".gitignore" -ErrorAction SilentlyContinue
$requiredProtections = @("ALMA.md", "*.local.md", "scripts/backup.log", ".session-stream.md", "*.skill-log.md")
foreach ($pattern in $requiredProtections) {
    if ($gitignore -notcontains $pattern) {
        $critical += "Missing .gitignore pattern: $pattern"
    }
}

if (Test-Path ".session-stream.md") {
    $buffer = Get-Content ".session-stream.md" -Raw
    if ($buffer -match "# FLUSHED") {
        $info += "Buffer clean: FLUSHED marker found."
    } elseif ($buffer -match "FLUSH_READY|SESSION_IDLE") {
        $info += "Buffer has auto-capture data pending FLUSH. Agent should consolidate on next interaction."
    } elseif ($buffer -match "# FLUSHING") {
        $critical += "Buffer in FLUSHING state. Crash recovery needed."
    } elseif ($buffer -match "AUTO-SESSION") {
        $info += "Buffer has auto-captured observations. Will be consolidated on next FLUSH."
    } else {
        $critical += "Buffer in raw state. Crash recovery needed."
    }
} else {
    $warning += "Buffer file not found. Will be created on next interaction."
}

$coreFiles = @("SKILL.md", "SOUL.md", "USER.md", "PROTOCOL.md", "AGENTS.md", "IDENTITY.md")
foreach ($f in $coreFiles) {
    if (-not (Test-Path $f)) {
        $critical += "Core file missing: $f"
    }
}

# WARNING

$ahead = git log --oneline origin/master..HEAD 2>$null
$behind = git log --oneline HEAD..origin/master 2>$null
if ($ahead) {
    $count = ($ahead | Measure-Object).Count
    $warning += "Local ahead of remote by $count commit(s). Push needed."
}
if ($behind) {
    $count = ($behind | Measure-Object).Count
    $warning += "Local behind remote by $count commit(s). Pull needed."
}

$task = schtasks /QUERY /TN "KAI Backup Soul" 2>$null
if ($task) {
    $info += "Backup task found in Task Scheduler."
} else {
    $warning += "Backup task not found in Task Scheduler."
}

if (Test-Path "ALMA.md") {
    $info += "ALMA.md present."
} else {
    $warning += "ALMA.md not found."
}

$lastCommit = git log --oneline -1 2>$null
$info += "Last commit: $lastCommit"

# REPORT

Write-Host "KAI Health Check Report"
Write-Host ""

if ($critical.Count -gt 0) {
    Write-Host "CRITICAL - $($critical.Count) issue(s):"
    foreach ($c in $critical) {
        Write-Host "  [FIX] $c"
    }
    Write-Host ""
}

if ($warning.Count -gt 0) {
    Write-Host "WARNING - $($warning.Count) issue(s):"
    foreach ($w in $warning) {
        Write-Host "  [WARN] $w"
    }
    Write-Host ""
}

if ($info.Count -gt 0) {
    Write-Host "INFO:"
    foreach ($i in $info) {
        Write-Host "  [OK] $i"
    }
}

Pop-Location

if ($critical.Count -gt 0) {
    exit 1
}
exit 0

