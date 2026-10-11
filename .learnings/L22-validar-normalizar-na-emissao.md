# Lição 22 — Valide e normalize na emissão; nunca trunque o que o usuário precisa copiar

**Data:** 2026-10-08 · **Origem:** SigmaFlow — fluxo do cliente de licença (REX #1/#3) · **Tags:** licenca, emissor, validacao, normalizacao, fingerprint, gui, fronteira, copiavel

## Os dois defeitos (a mesma raiz)

O fluxo de ativação offline do SigmaFlow tinha duas lacunas espelhadas:

1. **GUI truncava o fingerprint** em 16 dos 64 hex para "caber no label". O cliente
   não conseguia enviar o código inteiro ao emissor → licença vinculada emitida com o
   trecho nunca ativava.
2. **O emissor não validava `--maquina`**: qualquer erro de dígito gerava chave
   ASSINADA que falhava só na máquina do cliente (`MaquinaDiferente`), longe de quem
   emitiu. Pior: fingerprint digitado em **maiúsculas** passava direto e nunca casava
   com o `sha256().hexdigest()` (sempre lowercase) usado na comparação.

A raiz é uma: **o sistema confiou que o dado atravessaria a fronteira intacto** —
do label ao clipboard, do clipboard ao email, do email ao CLI, do payload ao `==`.

## O princípio (família L15/L18 — instrumento vs alvo)

- **Quem assina/emite é a fronteira que pode baratar o erro.** Validar e normalizar
  ANTES de produzir o artefato assinado custa zero; depois de emitido, o erro só
  aparece em outro processo, em outra máquina, sem chance de correção.
- **Comparação byte-a-byte exige normalização no nascimento.** Hash/identificador que
  será comparado com `==` deve ser normalizado (lowercase, strip) no EMISSOR e não
  apenas no receptor — o receptor "consertar" esconde quem errou.
- **Identificador que o usuário precisa copiar integralmente nunca é truncado para
  display.** Truncamento é ok em log/telemetria; em tela onde o valor é o INPUT de um
  fluxo manual, truncar é quebrar o fluxo. Se não cabe: mono font + botão Copiar.
- **Teste do caminho inteiro emissor→receptor** (end-to-end com chave emitida e
  ativada) é o único que pega a discórdia de forma entre as duas bordas; teste de
  unidade em cada borda passa com as duas erradas em direções opostas.

## Detalhe operacional (o guard pegou a mim)

A primeira versão do botão Copiar trouxe `try: update_idletasks() except: pass` —
o guard R56 (`except: pass` sem revisão) reprovou na suíte. O `update_idletasks`
não precisa de proteção; remover o swallowing foi o fix honesto. Guard que pega a
própria autora é guard funcionando.

## Licao

**Valide e normalize na fronteira que produz o artefato; trate o identificador do
usuário como dado de entrada de um fluxo, não como enfeite de UI.** Emitir barato,
receber caro é a inversão errada — e é exatamente o que sistemas offline de licença
(among others) fazem por default.

## Metadata

**Logged:** 2026-10-08
**Priority:** medium
**Status:** active
**Project:** inpi-marcas-patentes
**Area:** licenca / gui / emissor
**Pattern-Key:** validar-normalizar-na-emissao
**Source:** REX `## Bloco:fluxo-licenca-cliente` (A1/A2); commits `df22f70`→esta rodada
**Related Files:** `src/gui_main.py`, `scripts/gerar_licenca.py`, `tests/test_license_fluxo_gui.py`, `tests/test_gerar_licenca_cli.py`
**Tags:** licenca, emissor, validacao, normalizacao, lowercase, fingerprint, truncamento, gui, fronteira, end-to-end
