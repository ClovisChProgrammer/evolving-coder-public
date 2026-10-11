# Lição 18 — Registro de teste e registro jurídico são indistinguíveis na forma

**Data:** 2026-09-27 · **Origem:** rodada +09 do SIGMAFLOW (P-15) · **Tags:** teste, fixture, contaminacao, dados, prova, remove-para-provar

## O sintoma

O `data/` do usuário continha o processo `824184185` — marca "CLOVIS CHARLANTI", classe 35,
concessão em 2021, **validade 15/01/2030**, status `registrada`. O `DUVIDAS+09` descrevia
aquilo como um processo do usuário presente apenas no espelho, a um salvamento da GUI de
ser apagado, e afirmava que a KAI o havia "resgatado" para o banco (79 → 80).

**Não era processo do usuário.** Era o valor da fixture `processo_marca` em
`tests/conftest.py`, vazado para o `data/` real. O registro real é `SIGMARCAS`, id
`929865014`, validade **2034-11-05**, e nunca foi tocado.

## A causa

Caminho de banco relativo + `chdir` do conftest insuficiente ⇒ a fixture escrevia no
`data/` real. Pior: a fixture tem **a mesma forma** de um registro de INPI — id numérico
de 9 dígitos, marca, validade, status. Nada no dado distingue um do outro.

## O raciocínio que produziu a conclusão errada

O diagnóstico "o espelho está adiantado em relação ao banco" era **verdadeiro**. O erro foi
a segunda inferência: ler espelho adiantado como "o banco está atrasado", sem considerar
que a diferença pudesse ser um artefato de teste, e não um registro perdido.

Regra de sinais, em ordem de força:

| Sinal | Leitura |
|---|---|
| **Contagem SOBE depois de um "resgate"** | Romanização: ou havia algo para resgatar (e a contagem anterior estava errada), ou você acabou de importar sujeira. Confira a procedência antes de comemorar. |
| Id com 9 dígitos, "válido", mas que não aparece no INPI | Fixture até prova em contrário |
| Marca/titular que o usuário não reconhece | Fixture, mesmo que completo e plausível |
| Dado que "estava só no espelho" e por isso "ia ser apagado" | A pergunta certa não é "como salvo?" mas "por que chegou ali?" |

## A ação correta foi remover — e ela prova mais que a inserção

Adicionar um registro "resgatado" cria um caminho novo, nunca testado, e produz uma base
maior que parece mais correta. **Remover** e conferir que o sistema continua coerente
(`foreign_key_check` sem violação, zero órfãos, espelho sincronizado, 79 = 79) prova
que o registro não era referenciado por nada.

É a disciplina **prove-by-removal**: quando a procedência de um dado é incerta, a
verificação que decide é a que **retira** e observa a coerência, não a que **acrescenta**
e observa o sucesso. Acrescentar prova que algo pode ser adicionado. Removendo e
mantendo-se inteiro, prova-se que aquilo não pertencia.

Relacionado: Lição 15 (verificação que passa sem provar) e o fato de que aqui a
verificação *falhou* e foi justamente isso que impediu o erro de virar commit — os dois
testes de CLI que escrevi com premissa errada quebraram, e a quebra era o sinal.

## Regra de ouro

**Antes de resgatar, preservar, restaurar ou "corrigir" um dado: prove de onde ele veio.**
Uma linha de proveniência vale mais que uma transação transacional. Se a proveniência for
um `conftest.py`, o resgate é o próprio erro — e a versão "corrigida" da base fica maior e
mais errada do que a original.

## Metadata

Source: sessão SigmaFlow rodada +09 (2026-09-27)
Related Files: tests/conftest.py, data/sigmaflow.db, data/processos.json, BLUEPRINT/DUVIDAS+09.md, data/pre-normalizacao-p15/
Pattern-Key: fixture-vs-real-record-prove-by-removal
