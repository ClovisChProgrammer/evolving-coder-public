---
name: system-beeps-off-by-default-rate-limited
description: "Padrao para agentes desktop persistentes (sprite/tray/daemon) com efeitos sonoros: sons OFF por padrao (opto-in), rate-limit global de beeps (~30s), e revisao dos triggers de emissao — apenas transicoes reais de estado produzem som, nunca cliques/interacoes discretas. Use ao construir ou diagnosticar agentes persistentes que tocam sons de notificacao do sistema, ou quando o usuario relatar 'alarme/beep estranho' vindo de um agente."
---

# System Beeps Off By Default Rate Limited

Qualquer agente desktop persistente com audio (sprite, tray, daemon, assistente residente) deve nascer mudo. Som e opt-in, limitado por taxa, e reservado a transicoes reais de estado — nunca a interacoes discretas.

Isso surgiu de um incidente real: um sprite residente tocava `winsound.MessageBeep` em interacoes (clique=asterisco, erro=mao, shutdown=beep padrao). O usuario relatou que soava como "alarme de bateria fraca" a cada pulso de presenca, com a bateria saudavel. Causa raiz: 3 gatilhos legitimos mas excessivos + 2 regex de deteccao com falso-positivo.

## Quick Reference

| Situation | Action |
|-----------|--------|
| Construindo agente desktop persistente com som | `sounds_enabled=False` como default; opt-in via menu/preferencia persistida |
| Agente emite som a cada interacao | Rate-limit global (minimo ~30s entre beeps) |
| Regex/parser decide quando emitir som | Apenas sinais estruturais (fim real de resposta/transicao de estado), nunca texto solto |
| Usuario relata "alarme/alerta" de um agente | Mapear os beeps nativos e reproduzir com o usuario para identificar quais incomodam; nao assumir bug de bateria |
| Clique/selecao/bob da janela | NAO devem produzir som — apenas transicoes reais de estado |

## Usage

Regras de design para qualquer agente persistente com audio:

1. **Off by default**: `sounds_enabled=False` por padrao. Para ativar, menu contextual/preferencia persistida pelo usuario.
2. **Rate-limit global**: constante unica de intervalo (ex.: `SOUND_MIN_GAP_MS=30000`) — no maximo 1 som por janela, independente de qual gatilho disparou.
3. **Reveja os triggers de emissao**: clique, hover, selecao e interacoes discretas NAO produzem som. Som so em transicoes reais: erro fatal, shutdown, notificacao de relevancia, milestone em borda.
4. **Endureca parsers de texto**: se regex decide silenciosamente (ex.: "parece erro", "resposta final"), exija sinais estruturais (fim de resposta, delimitador), nao keywords soltas — senao ha falso-positivo.
5. **Estado persistido**: preferencia de som guardada em config (ex.: sprite-pos.json) para sobreviver a restart.

### Validacao

Teste unitario padrao:
- Sounds off → nenhuma chamada de beep emitida.
- 2a chamada em <30s → suprimida (rate-limit funciona).
- Chamada apos 31s → toca (intervalo renovado).
- Monkeypatch do modulo de som nativo para nao tocar de verdade no teste.

## Examples

Caso real (sprite KAI, 2026-09-18):

- Sintoma: usuario ouvia "alarme de bateria fraca" a cada pulso de presenca (bateria saudavel). Eram 3 `winsound.MessageBeep` (MB_ICONASTERISK, MB_ICONHAND, MB_OK) + 2 regex falso-positivas:
  - `isFinalSignoff` marcava shutdown no MEIO da resposta (nao exigia fim da resposta).
  - `looksLikeError` pegava "nao foi encontrado"/"falha critica" de texto comum → 121 error-hit no log.
- Fix:
  - `sounds_enabled=False` default + token de persistencia.
  - `SOUND_MIN_GAP_MS=30000`.
  - Milestone sonoro so em borda; clique sem milestone.
  - Regex endurecidas (`isFinalSignoff` exige fim da resposta; `looksLikeError` so sinais estruturais).
- Validacao: teste unitario monkeypatch do `winsound` (off silencia, 2a chamada <30s suprimida, apos 31s toca); regex 8/8; deploy paritario SHA256; sprite religado silencioso. Commit 341142c.

## Source Learning

This skill was extracted from a learning entry.
- Learning ID: LRN-20260918-001
- Original File: .learnings/LEARNINGS.md