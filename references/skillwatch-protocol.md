# Protocolo SkillWatch — Referência Detalhada

> Este arquivo é lido SOB DEMANDA — quando uma skill é carregada.
> Não é injetado a cada chamada de API.

## Regras

### 1. Anúncio a Cada Carga de Skill

Sempre que uma skill for carregada (por matching automático ou carga explícita), eu DEVO:

- **No início do uso**: `🔧 SkillWatch: carreguei [skill] ([N linhas]) — [motivo]`
- **Exemplo**: `🔧 SkillWatch: carreguei frontend-design (452L) — você pediu revisão do site NAVINCLUD`

### 2. Log Persistente por Projeto

Cada projeto mantém seu próprio registro em `.skill-log.md` na raiz do projeto:

```
# Skill Log — [Nome do Projeto]

## Sessão YYYY-MM-DD

| # | Skill | Linhas | Motivo | Instância |
|---|-------|--------|--------|-----------|
| 1 | evolving-coder | 312L | Startup obrigatório | automática |
| 2 | frontend-design | 452L | Revisão de UI | matching |
```

### 3. Sumário ao Final de Cada Sessão

Antes de encerrar ou mudar de projeto, devo apresentar:

```
📊 SkillWatch — Resumo da Sessão
   Skills carregadas: [N]
   Skills únicas usadas: [N]
   Total de linhas processadas: [N]
   Skills mais usadas: [top 3]
```
