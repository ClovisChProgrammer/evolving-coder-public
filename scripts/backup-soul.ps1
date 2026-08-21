<#
.SYNOPSIS
    KAI Soul Backup — commit + push do repositório evolving-coder.
.DESCRIPTION
    Faz git add -u (só tracked files), commit com timestamp e push para o GitHub.
    Seguro para executar via Agendador de Tarefas do Windows.
    NÃO commit arquivos untracked (ALMA.md, USER.local.md, etc. protegidos).
.EXAMPLE
    .\scripts\backup-soul.ps1
.NOTES
    Versão: 2.0
    Autor: KAI
    Segurança: usa git add -u (não -A) para jamais commitar arquivos não-tracked.
#>

$repoPath = "C:\Users\clovi\.config\opencode\skills\evolving-coder"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$logFile = Join-Path $repoPath "scripts\backup.log"

# Verificar se o diretório existe
if (-not (Test-Path -LiteralPath $repoPath)) {
    $msg = "$timestamp — ERRO: Diretório $repoPath não encontrado."
    $msg | Out-File -Append $logFile
    Write-Host "[KAI] $msg"
    exit 1
}

try {
    Push-Location $repoPath

    $status = git status --porcelain
    if (-not $status) {
        "$timestamp — Nada a commit. Repositório limpo." | Out-File -Append $logFile
        Write-Host "[KAI] Nada a commitar. Repositório limpo."
        return
    }

    # Usar git add -u (apenas tracked files) — NUNCA git add -A
    # Isso protege arquivos untracked como ALMA.md, USER.local.md, etc.
    git add -u

    $commitResult = git commit -m "KAI backup $timestamp" 2>&1
    $commitExitCode = $LASTEXITCODE

    if ($commitExitCode -ne 0) {
        "$timestamp — ERRO no commit: $commitResult" | Out-File -Append $logFile
        Write-Host "[KAI] ERRO no git commit. Verifique o log."
        Pop-Location
        exit 1
    }

    # Pull rebase antes do push para evitar rejeição por divergência
    git pull --rebase 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        # Se rebase falhar, abortar e avisar
        git rebase --abort 2>&1 | Out-Null
        "$timestamp — ERRO no git pull --rebase. Remote pode ter divergido." | Out-File -Append $logFile
        Write-Host "[KAI] ERRO: conflito no rebase. Resolva manualmente."
        Pop-Location
        exit 1
    }

    $pushResult = git push 2>&1
    if ($LASTEXITCODE -eq 0) {
        "$timestamp — Backup concluído com sucesso." | Out-File -Append $logFile
        Write-Host "[KAI] Backup concluído com sucesso."
    } else {
        "$timestamp — ERRO no push: $pushResult" | Out-File -Append $logFile
        Write-Host "[KAI] ERRO no git push. Verifique conexão e credenciais."

        # Tenta notificação visual no Windows
        try {
            Add-Type -AssemblyName System.Windows.Forms
            $notify = New-Object System.Windows.Forms.NotifyIcon
            $notify.Icon = [System.Drawing.SystemIcons]::Warning
            $notify.BalloonTipTitle = "KAI Backup Failed"
            $notify.BalloonTipText = "git push falhou. Verifique backup.log"
            $notify.Visible = $true
            $notify.ShowBalloonTip(5000)
            Start-Sleep -Milliseconds 100
            $notify.Dispose()
        } catch {
            # Notificação visual é bônus, não crítica
        }
    }
}
catch {
    "$timestamp — EXCEÇÃO: $_" | Out-File -Append $logFile
    Write-Host "[KAI] EXCEÇÃO: $_"
}
finally {
    Pop-Location
}

# Manter log com no máximo 100 linhas (rotação simples)
try {
    $logContent = Get-Content -Path $logFile
    if ($logContent.Count -gt 100) {
        $logContent[-100..-1] | Set-Content -Path $logFile
    }
} catch {
    # Rotação de log é bônus, não crítica
}
