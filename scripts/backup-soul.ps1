<#
.SYNOPSIS
    KAI Soul Backup â€” commit + push do repositÃ³rio evolving-coder.
.DESCRIPTION
    Faz git add -u (sÃ³ tracked files), commit com timestamp e push para o GitHub.
    Seguro para executar via Agendador de Tarefas do Windows.
    NÃƒO commit arquivos untracked (ALMA.md, USER.local.md, etc. protegidos).
.EXAMPLE
    .\scripts\backup-soul.ps1
.NOTES
    VersÃ£o: 2.0
    Autor: KAI
    SeguranÃ§a: usa git add -u (nÃ£o -A) para jamais commitar arquivos nÃ£o-tracked.
#>

$repoPath = "$PSScriptRoot\.."
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$logFile = Join-Path $repoPath "scripts\backup.log"

# Verificar se o diretÃ³rio existe
if (-not (Test-Path -LiteralPath $repoPath)) {
    $msg = "$timestamp â€” ERRO: DiretÃ³rio $repoPath nÃ£o encontrado."
    $msg | Out-File -Append $logFile
    Write-Host "[KAI] $msg"
    exit 1
}

try {
    Push-Location $repoPath

    $status = git status --porcelain
    if (-not $status) {
        "$timestamp â€” Nada a commit. RepositÃ³rio limpo." | Out-File -Append $logFile
        Write-Host "[KAI] Nada a commitar. RepositÃ³rio limpo."
        return
    }

    # Usar git add -u (apenas tracked files) â€” NUNCA git add -A
    # Isso protege arquivos untracked como ALMA.md, USER.local.md, etc.
    git add -u

    $commitResult = git commit -m "KAI backup $timestamp" 2>&1
    $commitExitCode = $LASTEXITCODE

    if ($commitExitCode -ne 0) {
        "$timestamp â€” ERRO no commit: $commitResult" | Out-File -Append $logFile
        Write-Host "[KAI] ERRO no git commit. Verifique o log."
        Pop-Location
        exit 1
    }

    # Pull rebase antes do push para evitar rejeiÃ§Ã£o por divergÃªncia
    git pull --rebase 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        # Se rebase falhar, abortar e avisar
        git rebase --abort 2>&1 | Out-Null
        "$timestamp â€” ERRO no git pull --rebase. Remote pode ter divergido." | Out-File -Append $logFile
        Write-Host "[KAI] ERRO: conflito no rebase. Resolva manualmente."
        Pop-Location
        exit 1
    }

    $pushResult = git push 2>&1
    if ($LASTEXITCODE -eq 0) {
        "$timestamp â€” Backup concluÃ­do com sucesso." | Out-File -Append $logFile
        Write-Host "[KAI] Backup concluÃ­do com sucesso."
    } else {
        "$timestamp â€” ERRO no push: $pushResult" | Out-File -Append $logFile
        Write-Host "[KAI] ERRO no git push. Verifique conexÃ£o e credenciais."

        # Tenta notificaÃ§Ã£o visual no Windows
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
            # NotificaÃ§Ã£o visual Ã© bÃ´nus, nÃ£o crÃ­tica
        }
    }
}
catch {
    "$timestamp â€” EXCEÃ‡ÃƒO: $_" | Out-File -Append $logFile
    Write-Host "[KAI] EXCEÃ‡ÃƒO: $_"
}
finally {
    Pop-Location
}

# Manter log com no mÃ¡ximo 100 linhas (rotaÃ§Ã£o simples)
try {
    $logContent = Get-Content -Path $logFile
    if ($logContent.Count -gt 100) {
        $logContent[-100..-1] | Set-Content -Path $logFile
    }
} catch {
    # RotaÃ§Ã£o de log Ã© bÃ´nus, nÃ£o crÃ­tica
}

