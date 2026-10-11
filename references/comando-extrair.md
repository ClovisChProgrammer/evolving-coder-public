# Comando EXTRAIR! — Extração de Skills (v2)

## O que é

Pipeline de extração de skills reutilizáveis. Antes conhecido como "Pipeline Extração de Skills". **v2** — agora com gatilho manual curto `EXTRAIR!`, critério de qualidade e passo de conflito.

## Ativação

### Automática (APRENDA! detecta)
Quando uma entry em `.learnings/` atinge `Status: promoted_to_skill`:
1. Extrair o Pattern-Key e o nome da entrada como skill-name
2. Executar: `scripts/extract-skill.ps1 <skill-name> -DryRun`
3. Apresentar o esqueleto ao usuário
4. Se aprovado, executar sem `-DryRun` e atualizar a entry original

### Manual (usuário pede diretamente)
Quando o usuário digita `EXTRAIR!` (linha isolada) ou `EXTRAIR! <skill-name>`:
- Cobre o caso de skills pedidas EXPLICITAMENTE, sem passar por `.learnings/`
- Mesmo fluxo: dry-run → aprovação → execução

## Critério de Qualidade (antes de extrair)

Só extrair quando:
- O padrão ocorre **≥2x** em projetos diferentes, OU
- O padrão é **óbvio** (skill única, padrão consolidado, relevância imediata clara)

Se o padrão ocorreu apenas 1x e não é óbvio → registrar em `.learnings/` e esperar maturar.

## Passo de Conflito (obrigatório)

Antes de extrair:
1. Verificar se já existe skill similar em `~/.config/opencode/skills/` ou `~/.agents/skills/`
2. Se similar existe → **fundir** (atualizar a existente com o novo padrão) ou **descartar** (se a existente cobre)
3. Se não existe → prosseguir com extração

## Fluxo de Execução

1. **Disparo** — automático (APRENDA!) ou manual (`EXTRAIR!`)
2. **Qualidade** — validar critério (≥2x ou óbvio)
3. **Conflito** — verificar duplicação com skills existentes
4. **Dry-run** — `scripts/extract-skill.ps1 <skill-name> -DryRun`
5. **Apresentar** ao usuário:
   - Nome sugerido
   - Path onde será criado
   - Gatilhos (Trigger conditions) sugeridos
6. **Aprovação** — usuário aprova
7. **Execução** — `scripts/extract-skill.ps1 <skill-name>` sem `-DryRun`
8. **Registro** — atualizar a entry original em `.learnings/`:
   - `Status: promoted_to_skill`
   - `Skill-Path: skills/<skill-name>`

## Proteção

- **Dry-run é OBRIGATÓRIO** antes de qualquer execução.
- **Aprovação do usuário é OBRIGATÓRIA** — nunca executar sem ela.
- Skills geradas sem aprovação explícita = violação de red line.