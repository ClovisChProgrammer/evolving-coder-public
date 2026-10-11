# 2026-08-23 — Commit Referenciou Asset Que Nunca Foi Adicionado

## Contexto
Commit cebee0d ("7a expressao pensando - arte nova...") descrevia a arte nova na mensagem, mas `assets/pensando.png` ficou untracked. O healthcheck só acusou o CRITICAL na sessão seguinte.

## Causa Raiz
Staging feito por lista seletiva sem conferir `git status --porcelain` contra os arquivos citados na mensagem de commit. Mensagem ≠ conteúdo verificado.

## Solução Aplicada
Commit corretivo 8bf801f + push dos 4 commits acumulados.

## Lição
**Antes de encerrar um commit, cruzar a mensagem com `git status --porcelain`**: todo arquivo citado na mensagem deve aparecer no diff staged. Passo novo no pré-shutdown mental.

## Status: resolved
