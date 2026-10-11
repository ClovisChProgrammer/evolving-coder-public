# start-kai-sprite.ps1 — Launcher manual do KAI Sprite
# Uso: .\start-kai-sprite.ps1 [-Exit] [-Kill]

param(
    [switch]$Exit,
    [switch]$Kill
)

$skillDir = Split-Path -Parent $PSScriptRoot
$script = Join-Path $skillDir "scripts\kai_sprite.py"
$exitMarker = Join-Path $skillDir ".kai-sprite.exit"

if ($Exit) {
    Write-Host "Saindo (persistente): marcando EXIT + matando processos KAI Sprite..."
    Set-Content -Path $exitMarker -Value (Get-Date -Format o) -Encoding ascii
    Get-Process python*, pythonw* -ErrorAction SilentlyContinue | Where-Object {
        try {
            $cmdline = (Get-CimInstance Win32_Process -Filter "ProcessId=$($_.Id)").CommandLine
            $cmdline -match "kai_sprite"
        } catch { $false }
    } | ForEach-Object {
        Write-Host "  Matando PID $($_.Id)"
        Stop-Process -Id $_.Id -Force
    }
    Write-Host "Pronto. O sprite permanecera fora ate voce iniciar (mesma semantica do botao Sair)."
    return
}

if ($Kill) {
    Write-Host "Matando processos KAI Sprite..."
    Get-Process python*, pythonw* -ErrorAction SilentlyContinue | Where-Object {
        try {
            $cmdline = (Get-CimInstance Win32_Process -Filter "ProcessId=$($_.Id)").CommandLine
            $cmdline -match "kai_sprite"
        } catch { $false }
    } | ForEach-Object {
        Write-Host "  Matando PID $($_.Id)"
        Stop-Process -Id $_.Id -Force
    }
    Write-Host "Pronto."
    return
}

# Invocacao manual: remove o marcador de saida persistente (desliga o respawn do watchdog)
if (Test-Path $exitMarker) {
    Remove-Item $exitMarker -Force
    Write-Host "Marcador de saida removido — watchdog volta a vigiar."
}

# Verificar se já está rodando
$existing = Get-Process python*, pythonw* -ErrorAction SilentlyContinue | Where-Object {
    try {
        $cmdline = (Get-CimInstance Win32_Process -Filter "ProcessId=$($_.Id)").CommandLine
        $cmdline -match "kai_sprite"
    } catch { $false }
}

if ($existing) {
    Write-Host "KAI Sprite já rodando (PID: $($existing.Id -join ', '))"
    $resp = Read-Host "Matar e reiniciar? (s/N)"
    if ($resp -eq "s") {
        $existing | Stop-Process -Force
        Start-Sleep -Seconds 1
    } else {
        Write-Host "Abortado."
        return
    }
}

# Encontrar pythonw
$py = $null
foreach ($cmd in @("pythonw", "python")) {
    $found = & where.exe $cmd 2>$null | Select-Object -First 1
    if ($found) { $py = $found; break }
}

if (-not $py) {
    Write-Host "ERRO: Python não encontrado no PATH"
    return
}

Write-Host "Iniciando KAI Sprite com $py..."
$proc = Start-Process -FilePath $py -ArgumentList $script -PassThru -WindowStyle Hidden
Start-Sleep -Seconds 1
if (-not $proc.HasExited) {
    Write-Host "KAI Sprite iniciado! PID: $($proc.Id)"
} else {
    Write-Host "ERRO: Sprite falhou ao iniciar"
}
