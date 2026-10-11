# Lição 20 — Contrato de repositório que aceita modelo, serviço que chama com kwargs

**Data:** 2026-09-28 · **Origem:** pós-rodada +11 do SIGMAFLOW (GUI Fluxo E) · **Tags:** contrato, servico, repositorio, kwargs, bug-silencioso, teste-nivel-servico

## O sintoma

`criar_tarefa_service` (`servico_fase2.py`) chamava `repositorio.criar_tarefa(titulo=..., descricao=..., processo_id=...)` com kwargs, mas `repositorio.criar_tarefa` espera um objeto `Tarefa` como primeiro argumento posicional. Resultado: **toda criação de tarefa falhava silenciosamente** — o serviço captura a exceção e devolve `{"ok": False, "erro": ...}`. A GUI mostrava erro genérico (não falso sucesso), o que é o comportamento defensivo correto, mas a feature simplesmente **não funcionava**.

## A causa raiz

Os outros fluxos da Fase 2 (Cliente, Documento, Evidência) seguem o padrão "serviço monta o modelo e chama `repo.criar_X(modelo, ...)`". O Fluxo E foi escrito com kwargs, quebrando o contrato do repositório. Pior: **nenhum teste dos 657 existentes exercitava `criar_tarefa_service` por esse caminho** — os serviços existiam e eram "testados", mas o teste não cobria o Fluxo E, então o bug vivia invisível.

## Sinais e leitura

| Sinal | Leitura |
|---|---|
| Serviço devolve `ok:False` com "got an unexpected keyword argument" | Contrato de assinatura quebrado entre camadas — o chamador usa kwargs, o receptor é posicional/objeto |
| Feature "existe" mas não persiste nada | Teste de **nível de serviço** ausente nesse fluxo específico |
| Serviço engole exceção e devolve dict de erro | Sem **log da causa** pode virar erro silencioso crônico (rolagem de sintomas) |

## Regra de ouro

**Todo serviço novo precisa de teste de nível de serviço que persiste de verdade** (banco `tmp_path`), não só de teste de GUI com monkeypatch. Testar a GUI com o serviço monkeypatchado **esconde** exatamente este tipo de contrato quebrado — a GUI testa o próprio handler, o serviço nunca roda. O bug só apareceu quando a GUI passou a chamar o serviço real (monkeypatch com `db_path=tmp`, não mock de função).

O padrão que funciona: monkeypatch **o serviço** redirecionando `db_path` para `tmp` (o serviço roda de verdade, o banco real nunca é tocado), em vez de substituir o serviço por um fake.

## Metadata

Source: sessão SigmaFlow pós-rodada +11 (2026-09-28)
Related Files: src/servico_fase2.py (criar_tarefa_service), src/repositorio.py (criar_tarefa), tests/test_fluxo_e_gui.py
Pattern-Key: servico-kwargs-vs-repositorio-modelo