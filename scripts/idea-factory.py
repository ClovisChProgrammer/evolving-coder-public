#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Idea Factory — Gerador de Insights baseado nas Skills do OpenCode
==================================================================
Extrai palavras-chave em português de todas as skills e oferece modos
de visualização, cruzamento aleatório e captura de ideias.

Uso:
  python idea-factory.py --genome              Genoma completo (agrupado)
  python idea-factory.py --genome --flat       Genoma completo (lista plana)
  python idea-factory.py --cross random        3 palavras de domínios diferentes
  python idea-factory.py --cross combo         2 domínios relacionados
  python idea-factory.py --seed "palavra"      1 sua + 2 de skills relacionadas
  python idea-factory.py --random              3 palavras aleatórias
  python idea-factory.py --random --weighted p1,p2  Enviesado por projetos
  python idea-factory.py --random --coinflip   Aleatório decide se pondera
  python idea-factory.py --capture             Modo interativo de captura
  python idea-factory.py --capture "X" --note "Y"  Captura direta
"""

import os, sys, re, json, random, datetime, argparse, pathlib, textwrap

if sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

SKILLS_DIR = pathlib.Path.home() / ".config" / "opencode" / "skills"
IDEA_BANK_PATH = pathlib.Path.cwd() / "IDEA_BANK.md"
PROJ_DIRS = [
    pathlib.Path.home() / "openclaw",
    pathlib.Path.home() / "OneDrive" / "Documents" / "Hermes-Agent",
    pathlib.Path.home() / "OneDrive" / "Documents" / "NAVINCLUD",
    pathlib.Path.home() / "OneDrive" / "Documents" / "QPEÇA",
]

DOMINIOS_PT = {
    "backend":     "Back-End e APIs",
    "frontend":    "Front-End e Web",
    "mobile":      "Mobile (Android, iOS, Flutter, RN)",
    "devops":      "DevOps e Infraestrutura",
    "security":    "Segurança e Auditoria",
    "testing":     "Testes e Qualidade",
    "cli":         "CLI e Terminal",
    "marketing":   "Marketing e Growth",
    "legal":       "Jurídico",
    "esoteric":    "Esotérico e Bem-Estar",
    "product":     "Produto e Estratégia",
    "research":    "Pesquisa Acadêmica",
    "docs":        "Documentos e Mídia",
    "utilities":   "Utilitários e Integrações",
    "ai":          "IA e Machine Learning",
    "gaming":      "Jogos e Criatividade",
    "other":       "Outros",
}

INFERENCIA_DOMINIO = {
    "fastapi-expert": "backend", "python-pro": "backend", "python-patterns": "backend",
    "nodejs-best-practices": "backend", "golang-pro": "backend",
    "rust-pro": "backend", "rust-engineer": "backend",
    "sql-pro": "backend", "postgres-pro": "backend",
    "graphql-architect": "backend", "api-patterns": "backend", "mcp-builder": "backend",
    "pandas-pro": "backend",
    "frontend-dev": "frontend", "frontend-design": "frontend",
    "tailwind-patterns": "frontend", "nextjs-react-expert": "frontend",
    "react-best-practices": "frontend", "web-design-guidelines": "frontend",
    "shader-dev": "frontend", "algorithmic-art": "frontend",
    "algorithmic-art-2": "frontend", "color-expert": "frontend",
    "clean-code": "frontend", "code-review-checklist": "frontend",
    "i18n-localization": "frontend", "documentation-templates": "frontend",
    "react-native-dev": "mobile", "flutter-dev": "mobile",
    "android-native-dev": "mobile", "minimax-android-native-dev": "mobile",
    "ios-application-dev": "mobile", "minimax-ios-application-dev": "mobile",
    "mobile-design": "mobile", "minimax-flutter-dev": "mobile",
    "minimax-react-native-dev": "mobile",
    "devops-engineer": "devops", "kubernetes-specialist": "devops",
    "terraform-engineer": "devops", "monitoring-expert": "devops",
    "sre-engineer": "devops", "deployment-procedures": "devops",
    "server-management": "devops", "performance-profiling": "devops",
    "vulnerability-scanner": "security", "red-team-tactics": "security",
    "codeql": "security", "semgrep": "security",
    "semgrep-rule-creator": "security", "semgrep-rule-variant-creator": "security",
    "sarif-parsing": "security", "differential-review": "security",
    "variant-analysis": "security", "audit-context-building": "security",
    "sharp-edges": "security", "insecure-defaults": "security",
    "property-based-testing": "security",
    "playwright-expert": "testing", "webapp-testing": "testing",
    "tdd-workflow": "testing", "testing-patterns": "testing",
    "lint-and-validate": "testing", "systematic-debugging": "testing",
    "test-master": "testing",
    "cli-developer": "cli", "bash-linux": "cli", "powershell-windows": "cli",
    "copywriting": "marketing", "copy-editing": "marketing",
    "cro": "marketing", "analytics": "marketing",
    "seo-audit": "marketing", "seo-fundamentals": "marketing",
    "programmatic-seo": "marketing", "schema": "marketing",
    "geo-fundamentals": "marketing", "ads": "marketing",
    "social": "marketing", "emails": "marketing",
    "marketing-ideas": "marketing", "marketing-psychology": "marketing",
    "launch": "marketing", "pricing": "marketing",
    "paywalls": "marketing", "signup": "marketing",
    "onboarding": "marketing", "popups": "marketing",
    "referrals": "marketing", "free-tools": "marketing",
    "competitors": "marketing", "ab-testing": "marketing",
    "brainstorm-okrs": "marketing",
    "contract-review-anthropic": "legal", "draft-nda": "legal",
    "nda-triage-anthropic": "legal", "nda-review-jamie-tso": "legal",
    "privacy-policy": "legal", "legal-risk-assessment-anthropic": "legal",
    "legal-risk-assessment-zacharie-laik": "legal",
    "mediation-dispute-analysis-jinzhe-tan": "legal",
    "statute-analysis-rafal-fryc": "legal",
    "tech-contract-negotiation-patrick-munro": "legal",
    "vendor-due-diligence-patrick-munro": "legal",
    "red-team-verifier-patrick-munro": "legal",
    "canned-responses-anthropic": "legal",
    "tabular-review-lawvable": "legal",
    "astrologia": "esoteric", "astrology-core": "esoteric",
    "mapa-astral": "esoteric", "numerologia": "esoteric",
    "numerologia-avancada": "esoteric", "advanced-numerology": "esoteric",
    "runas": "esoteric", "tarot": "esoteric",
    "mandalas": "esoteric", "geometria-sagrada": "esoteric",
    "binaural-neurofeedback": "esoteric", "art-philosophy": "esoteric",
    "nyx-archive-art-philosophy": "esoteric",
    "anxiety-relief": "esoteric", "depression-support": "esoteric",
    "mindfulness-meditation": "esoteric", "morning-routine": "esoteric",
    "zenplus-health": "esoteric",
    "architecture": "product", "microservices-architect": "product",
    "saas-architect-3x3ra": "product", "database-design": "product",
    "legacy-modernizer": "product", "app-builder": "product",
    "templates": "product", "behavioral-modes": "product",
    "brainstorming": "product", "plan-writing": "product",
    "prioritization-frameworks": "product", "stakeholder-map": "product",
    "summarize-interview": "product", "summarize-meeting": "product",
    "pre-mortem": "product", "ask-questions-if-underspecified": "product",
    "research-en": "research", "research-zh": "research",
    "research-codex-en": "research", "research-codex-zh": "research",
    "research-add-fields": "research", "research-add-items": "research",
    "research-deep": "research", "research-report": "research",
    "minimax-pdf": "docs", "minimax-docx": "docs",
    "minimax-xlsx": "docs", "pptx-generator": "docs",
    "minimax-pptx-generator": "docs", "minimax-minimax-pdf": "docs",
    "minimax-minimax-docx": "docs", "minimax-minimax-xlsx": "docs",
    "minimax-music-gen": "docs", "minimax-minimax-music-gen": "docs",
    "minimax-music-playlist": "docs", "minimax-minimax-music-playlist": "docs",
    "mmx-cli": "docs", "minimax-minimax-multimodal-toolkit": "docs",
    "minimax-vision-analysis": "docs",
    "minimax-gif-sticker-maker": "docs",
    "minimax-buddy-sings": "docs", "minimax-buddy-sings-minimax": "docs",
    "gws-calendar": "utilities", "gws-docs": "utilities",
    "gws-drive": "utilities", "gws-gmail": "utilities",
    "gws-shared": "utilities", "gws-sheets": "utilities",
    "gws-tasks": "utilities", "gws-workflow": "utilities",
    "spec-miner": "utilities", "grammar-check": "utilities",
    "evolving-coder": "utilities", "customize-opencode": "utilities",
    "find-skills": "utilities", "mcp-brasil-public-apis": "utilities",
    "game-development": "gaming",
    "paramus-chemistry": "other",
    "13-day-sprint-method": "product",
    "sovereign-rpg-xp-engine": "gaming",
    "zeitgaist-dialect": "other",
    "parallel-agents": "ai",
    "intelligent-routing": "ai",
    "prompt-engineer": "ai",
    "rag-architect": "ai",
    "intelligent-routing": "ai",
    "parallel-agents": "ai",
    "minimax-frontend-dev": "frontend",
    "minimax-fullstack-dev": "backend",
    "minimax-shader-dev": "frontend",
    "minimax-vision-analysis": "docs",
    "minimax-gif-sticker-maker": "docs",
    "minimax-buddy-sings": "docs",
}

PALAVRAS_CHAVE_PT = {
    "fastapi-expert": "api rápida, desempenho, async, pydantic, validação, autenticação jwt, websocket, openapi, swagger, python assíncrono",
    "python-pro": "python, tipagem, async, pytest, ruff, mypy, dataclass, injeção de dependência, logging, erros estruturados",
    "python-patterns": "python, framework, async, type hints, estrutura de projeto, boas práticas",
    "nodejs-best-practices": "node, javascript, express, async, segurança, arquitetura, npm",
    "golang-pro": "go, goroutine, channel, concorrência, microserviço, grpc, rest, pprof, teste tabelado",
    "rust-pro": "rust, async, tokio, axum, type system, sistemas, performance, segurança de memória",
    "rust-engineer": "rust, ownership, borrowing, lifetime, trait, async, tokio, resultado, opção",
    "sql-pro": "sql, consulta, janela, cte, índice, explain, join, agregação, otimização",
    "postgres-pro": "postgresql, jsonb, replicação, vacuum, extensão, explain, monitoramento",
    "graphql-architect": "graphql, schema, resolver, dataloader, apollo, federação, subscription, query",
    "api-patterns": "api, rest, graphql, trpc, versionamento, paginação, formato de resposta",
    "mcp-builder": "mcp, server, protocolo, ferramenta, recurso, padrão, modelo de contexto",
    "pandas-pro": "pandas, dataframe, join, pivot, série temporal, nan, agregação, transformação",
    "frontend-dev": "landing page, ui, animação, scroll, cinema, asset ia, copy, conversão",
    "frontend-design": "design, ui, layout, cor, tipografia, componente, estética, princípio",
    "tailwind-patterns": "tailwind, css, utilitário, design token, container query, responsivo",
    "nextjs-react-expert": "react, nextjs, performance, server component, suspense, bundle, otimização",
    "react-best-practices": "react, nextjs, performance, waterfall, bundle, servidor, cliente",
    "web-design-guidelines": "ui, revisão, acessibilidade, auditoria, diretriz, usabilidade",
    "shader-dev": "shader, glsl, ray marching, sdf, partícula, fluido, luz, pós-processamento",
    "algorithmic-art": "arte generativa, p5js, aleatório, seed, campo de fluxo, partícula, interactivo",
    "algorithmic-art-2": "arte algorítmica, generative art, código criativo, visual",
    "color-expert": "cor, teoria da cor, paleta, nome, espaço de cor, gradiente, acessibilidade, pigmento",
    "clean-code": "código limpo, conciso, direto, sem comentário, pragmático, legível",
    "code-review-checklist": "revisão, código, qualidade, segurança, boas práticas, checklist",
    "i18n-localization": "internacionalização, i18n, tradução, locale, rtl, string, localização",
    "documentation-templates": "documentação, readme, api, template, estrutura, ai-friendly",
    "react-native-dev": "react native, expo, componente, animação, navegação, estado, formulário, performance, teste, deploy",
    "flutter-dev": "flutter, riverpod, bloc, gorouter, widget, const, responsivo, teste, devtools",
    "android-native-dev": "android, kotlin, compose, material design 3, acessibilidade, build",
    "minimax-android-native-dev": "android, kotlin, compose, material design, acessibilidade, ui",
    "ios-application-dev": "ios, uikit, snapkit, swiftui, safe area, dark mode, acessibilidade, navegação",
    "minimax-ios-application-dev": "ios, swift, uikit, swiftui, interface, apple, mobile",
    "mobile-design": "design mobile, toque, gesto, performance, ios, android, padrão, plataforma",
    "minimax-flutter-dev": "flutter, dart, widget, multiplataforma, mobile, google",
    "minimax-react-native-dev": "react native, expo, mobile, javascript, ios, android",
    "devops-engineer": "docker, ci/cd, kubernetes, terraform, github actions, gitops, deploy, pipeline",
    "kubernetes-specialist": "kubernetes, helm, rbac, network policy, pod, deploy, service, gitops",
    "terraform-engineer": "terraform, iaC, módulo, estado, provedor, aws, azure, gcp, multi-ambiente",
    "monitoring-expert": "prometheus, grafana, logging, tracing, k6, alerta, dashboard, carga",
    "sre-engineer": "slo, sli, error budget, incidente, capacidade, toil, confiabilidade, sla",
    "deployment-procedures": "deploy, produção, rollback, canary, verificação, seguro, procedimento",
    "server-management": "servidor, processo, monitoramento, escalonamento, administração",
    "performance-profiling": "performance, medição, análise, otimização, perfil, gargalo",
    "vulnerability-scanner": "vulnerabilidade, owasp 2025, supply chain, ataque, superfície, risco",
    "red-team-tactics": "red team, mitre attack, fase de ataque, evasão, relatório, ofensivo",
    "codeql": "codeql, query, data flow, taint, varredura, sarif, segurança, análise estática",
    "semgrep": "semgrep, regra, scan, análise estática, vulnerabilidade, padrão, segurança",
    "semgrep-rule-creator": "semgrep, regra customizada, detecção, padrão de bug, segurança",
    "semgrep-rule-variant-creator": "semgrep, variante, linguagem, portabilidade, regra",
    "sarif-parsing": "sarif, parse, análise, resultado, dedup, ci/cd, formato",
    "differential-review": "revisão diferencial, diff, pr, commit, segurança, blast radius, cobertura",
    "variant-analysis": "análise de variante, vulnerabilidade, padrão, caça de bug, auditoria",
    "audit-context-building": "auditoria, contexto, linha por linha, análise profunda, arquitetura",
    "sharp-edges": "api propensa a erro, configuração perigosa, footgun, seguro por padrão",
    "insecure-defaults": "falha insegura, padrão, hardcoded, autenticação fraca, produção",
    "property-based-testing": "teste baseado em propriedade, serialização, validação, parsing",
    "playwright-expert": "playwright, e2e, page object, fixture, ci, visual regression, mock",
    "webapp-testing": "teste web, e2e, playwright, auditoria profunda, estratégia",
    "tdd-workflow": "tdd, red, green, refactor, ciclo, teste primeiro, desenvolvimento",
    "testing-patterns": "teste, unitário, integração, mock, padrão, estratégia",
    "lint-and-validate": "lint, formato, validação, tipo, análise estática, qualidade, pós-modificação",
    "systematic-debugging": "debug, 4 fases, causa raiz, evidência, verificação, metodologia",
    "test-master": "teste, geração, mock, cobertura, arquitetura de teste, plano, estratégia",
    "cli-developer": "cli, terminal, argumento, flag, subcomando, progresso, completions, commander, click",
    "bash-linux": "bash, linux, pipe, script, erro, terminal, shell, comando",
    "powershell-windows": "powershell, windows, cmdlet, operador, erro, script, automação",
    "copywriting": "copywriting, marketing, landing page, headline, cta, valor, persuasão, conversão",
    "copy-editing": "copy, edição, revisão, refresh, polimento, conteúdo, feedback",
    "cro": "cro, conversão, otimização, landing page, formulário, taxa, abandono, teste",
    "analytics": "analytics, ga4, gtm, evento, conversão, tracking, utm, atribuição, mixpanel",
    "seo-audit": "seo, auditoria, técnico, core web vitals, crawl, indexação, ranking, página",
    "seo-fundamentals": "seo, fundamento, eeat, algoritmo, google, core web vitals",
    "programmatic-seo": "seo programático, template, escala, página, keyword, directory, location",
    "schema": "schema markup, structured data, json-ld, rich snippet, google, busca",
    "geo-fundamentals": "geo, generative engine optimization, chatgpt, claude, perplexity, ia busca",
    "ads": "anúncio, google ads, meta, facebook, linkedin, ppc, roas, cpa, audiência, lance",
    "social": "social media, linkedin, twitter, instagram, tiktok, conteúdo, engajamento, shorts",
    "emails": "email, sequência, drip, nutrição, onboarding, automação, lifecycle, cadência",
    "marketing-ideas": "marketing, ideia, estratégia, crescimento, promoção, brainstorm",
    "marketing-psychology": "psicologia, comportamento, viés cognitivo, persuasão, decisão, framing, prova social",
    "launch": "lançamento, product hunt, gtm, waitlist, early access, checklist, anúncio",
    "pricing": "preço, tier, freemium, trial, packaging, valor, métrica, van westendorp, monetização",
    "paywalls": "paywall, upgrade, upsell, feature gate, conversão, free, premium, trial",
    "signup": "cadastro, signup, registro, trial, ativação, formulário, abandono, conversão",
    "onboarding": "onboarding, ativação, primeira experiência, time to value, aha moment, retenção",
    "popups": "popup, modal, exit intent, overlay, banner, lead, email, conversão",
    "referrals": "indicação, referral, afiliado, embaixador, boca a boca, viral, incentivo",
    "free-tools": "ferramenta gratuita, lead gen, seo, calculadora, gerador, auditoria, marketing",
    "competitors": "concorrente, comparação, vs page, alternativa, battle card, posicionamento",
    "ab-testing": "ab test, experimento, hipótese, variante, significância estatística, split test",
    "brainstorm-okrs": "okr, objetivo, key result, trimestre, alinhamento, meta, estratégia",
    "contract-review-anthropic": "contrato, revisão, cláusula, redline, playbook, negociação, desvio",
    "draft-nda": "nda, confidencialidade, acordo, sigilo, informação, parte, jurisdição",
    "nda-triage-anthropic": "nda, triagem, verde, amarelo, vermelho, risco, counsel, revisão",
    "nda-review-jamie-tso": "nda, revisão, cláusula, issue log, redline, fallback, rationales",
    "privacy-policy": "privacidade, política, dados, gdpr, lgpd, compliance, cookie, consentimento",
    "legal-risk-assessment-anthropic": "risco legal, severidade, probabilidade, classificação, escalation",
    "legal-risk-assessment-zacharie-laik": "pesquisa jurídica, goodlegal, mcp, jurisprudência, lei, frança, união europeia",
    "mediation-dispute-analysis-jinzhe-tan": "mediação, disputa, análise, posição, interesse, acordo, caucus, estratégia",
    "statute-analysis-rafal-fryc": "estatuto, regulamento, interpretação, legislação, compliance, intenção legislativa",
    "tech-contract-negotiation-patrick-munro": "negociação, contrato tech, b2b, posição, concessão, sla, ip, responsabilidade",
    "vendor-due-diligence-patrick-munro": "due diligence, vendor, fornecedor, risco, financeiro, operacional, compliance, gdpr",
    "red-team-verifier-patrick-munro": "verificação, fact-checking, fonte, qualidade, adversarial, jurídico, revisão",
    "canned-responses-anthropic": "resposta template, jurídico, inquiry, nda, discovery, hold, legal",
    "tabular-review-lawvable": "revisão tabular, documento, pdf, docx, coluna, excel, citação, matriz",
    "astrologia": "astrologia, signo, ascendente, casa astrológica, aspecto, mapa astral, compatibilidade",
    "astrology-core": "mapa astral, efeméride, flatlib, cálculo, ascendente, casa, aspecto, sinastria, trânsito",
    "mapa-astral": "mapa astral, carta astrológica, ascendente, casa, aspecto, sinastria, trânsito, ephemeris",
    "numerologia": "numerologia, caminho de vida, destino, alma, personalidade, compatibilidade, ciclo",
    "numerologia-avancada": "numerologia, pitagórico, caldeu, kabbalah, anjos, dívida cármica, número composto",
    "advanced-numerology": "numerologia, pitagórico, caldeu, redução, mestre, karma, pináculo, ciclo, kabbalah",
    "runas": "runas, elder futhark, sorteio, spread, significado, oráculo, viking",
    "tarot": "tarot, arcano, leitura, spread, significado, carta, oráculo, interpretação",
    "mandalas": "mandala, meditação, círculo, símbolo, autoconhecimento, criação, interpretação",
    "geometria-sagrada": "geometria sagrada, sólido platônico, espiral áurea, fractal, proporção divina, harmonia",
    "binaural-neurofeedback": "frequência sonora, tom binaural, onda cerebral, meditação, foco, relaxamento, neurofeedback",
    "art-philosophy": "filosofia da arte, linguagem visual, cor, composição, significado, fallibilismo, jogo",
    "nyx-archive-art-philosophy": "arte, filosofia, linguagem visual, teoria da cor, composição, estética, autoral",
    "anxiety-relief": "ansiedade, alívio, técnica, respiração, relaxamento, acolhimento, exercício",
    "depression-support": "depressão, apoio, acolhimento, saúde mental, escuta, recurso",
    "mindfulness-meditation": "mindfulness, meditação, atenção plena, respiração, corpo, momento presente",
    "morning-routine": "rotina matinal, manhã, hábito, produtividade, bem-estar, otimização",
    "zenplus-health": "saúde, bem-estar, zen, equilíbrio, corpo, mente, qualidade de vida",
    "architecture": "arquitetura, decisão, trade-off, requisito, adr, análise, sistema, design",
    "microservices-architect": "microserviço, distribuído, ddd, saga, cqrs, event sourcing, service mesh, monólito",
    "saas-architect-3x3ra": "saas, arquitetura, segurança, monetização, escalabilidade, 3x3ra, planejamento",
    "database-design": "banco de dados, schema, índice, orm, serverless, indexação, modelagem",
    "legacy-modernizer": "legado, migração, strangler fig, monólito, dívida técnica, modernização, api facade",
    "app-builder": "aplicação, fullstack, scaffolding, linguagem natural, orquestrador, stack",
    "templates": "template, scaffold, projeto, boilerplate, estrutura, inicialização, 12 templates",
    "behavioral-modes": "modo, brainstorm, implementar, debug, revisar, ensinar, ship, orquestrar",
    "brainstorming": "brainstorm, socrático, pergunta, requisito, feature, exploração, ideação",
    "plan-writing": "plano, tarefa, breakdown, dependência, verificação, multi-passo, implementação",
    "prioritization-frameworks": "priorização, rice, ice, kano, moscow, opportunity score, framework, decisão",
    "stakeholder-map": "stakeholder, mapa, poder, interesse, grade, comunicação, plano, alinhamento",
    "summarize-interview": "entrevista, resumo, jtbd, satisfação, ação, cliente, descoberta, síntese",
    "summarize-meeting": "reunião, resumo, ata, decisão, ação, participante, tópico, minuta",
    "pre-mortem": "pre-mortem, risco, tiger, paper tiger, elefante, lançamento, prd, análise",
    "ask-questions-if-underspecified": "perguntar, esclarecer, requisito, dúvida, antes de implementar, ambiguidade",
    "research-en": "pesquisa, outline, tópico, investigação, benchmark, inglês, acadêmico",
    "research-zh": "pesquisa, outline, tópico, investigação, chinês, acadêmico",
    "research-codex-en": "codex, pesquisa, metodologia, referência, inglês, acadêmico",
    "research-codex-zh": "codex, pesquisa, metodologia, referência, chinês, acadêmico",
    "research-add-fields": "pesquisa, campo, definição, outline, estrutura, adicionar",
    "research-add-items": "pesquisa, item, objeto, outline, adicionar, lista",
    "research-deep": "pesquisa profunda, agente, item, outline, investigação, autônomo",
    "research-report": "pesquisa, relatório, markdown, sumário, campo, resultado, documentação",
    "minimax-pdf": "pdf, documento, relatório, proposta, currículo, design, impressão, profissional",
    "minimax-docx": "docx, word, documento, relatório, contrato, formatação, openxml",
    "minimax-xlsx": "excel, planilha, xlsx, fórmula, tabela, financeiro, modelo, dado, análise",
    "pptx-generator": "powerpoint, pptx, apresentação, slide, deck, cover, toc, gráfico",
    "minimax-pptx-generator": "powerpoint, pptx, slide, apresentação, deck, conteúdo",
    "minimax-music-gen": "música, som, audio, canção, letra, melodia, produção, composição, ia",
    "minimax-music-playlist": "playlist, música, personalizado, perfil, gosto, recomendação, curadoria",
    "mmx-cli": "multimodal, texto, imagem, vídeo, audio, música, ia, geração, minimax, cli",
    "minimax-vision-analysis": "visão, imagem, análise, descrição, ocr, diagrama, gráfico, wireframe, foto",
    "minimax-gif-sticker-maker": "gif, sticker, animado, funko, pop, cartoon, avatar, expressão, emoji",
    "minimax-buddy-sings": "música, pet, buddy, cantar, canção, amigo, companheiro, áudio",
    "gws-calendar": "google calendar, calendário, evento, agenda, compromisso, lembretes",
    "gws-docs": "google docs, documento, texto, editor, colaboração, escrita, leitura",
    "gws-drive": "google drive, arquivo, pasta, compartilhamento, nuvem, armazenamento",
    "gws-gmail": "gmail, email, mensagem, enviar, ler, caixa de entrada, comunicação",
    "gws-shared": "gws, cli, autenticação, flag, formato, padrão, google workspace",
    "gws-sheets": "google sheets, planilha, célula, fórmula, dado, tabela, colaboração",
    "gws-tasks": "google tasks, tarefa, lista, afazer, pendência, lembretes, organização",
    "gws-workflow": "produtividade, workflow, google, integração, automatização, tarefa, serviço",
    "spec-miner": "engenharia reversa, legado, sem documento, especificação, análise, arquitetura",
    "grammar-check": "gramática, revisão, erro, fluxo, texto, escrita, correção, prova",
    "evolving-coder": "identidade, aprendizado, skill, extração, evolução, kai, protocolo, alma",
    "customize-opencode": "opencode, config, json, skill, agente, mcp, plugin, permissão, setup",
    "find-skills": "skill, descoberta, instalação, funcionalidade, search, encontrar",
    "mcp-brasil-public-apis": "brasil, api pública, legislação, economia, transparência, judiciary, dado governo",
    "game-development": "jogo, desenvolvimento, motor, plataforma, orquestrador, roteamento",
    "paramus-chemistry": "química, paramus, elemento, reação, laboratório, ciência",
    "13-day-sprint-method": "sprint, 13 dias, metodologia, agil, entrega, ciclo, produto",
    "sovereign-rpg-xp-engine": "rpg, xp, engine, soberano, jogo, experiência, level, progressão",
    "zeitgaist-dialect": "dialeto, zeitgaist, fala, comunicação, sotaque, coaching, linguagem",
    "intelligent-routing": "roteamento inteligente, agente, task, especialista, seleção, orquestração",
    "parallel-agents": "multi-agente, paralelo, orquestração, domínio, análise, perspectiva, task",
    "prompt-engineer": "prompt, engenharia, llm, template, schema, chain of thought, avaliação, rubrica",
    "rag-architect": "rag, vector store, embedding, chunking, retrieval, rerank, hyde, busca semântica",
    "minimax-frontend-dev": "frontend, ui, animação, asset ia, copy, landing page, visual, premium",
    "minimax-fullstack-dev": "fullstack, backend, frontend, integração, api, rest, auth, upload, real-time",
    "minimax-shader-dev": "shader, glsl, efeito visual, partícula, sdf, ray marching, fluido, luz",
}

def carregar_skills():
    skills = []
    if not SKILLS_DIR.exists():
        print(f"[ERRO] Diretorio de skills nao encontrado: {SKILLS_DIR}", file=sys.stderr)
        sys.exit(1)
    for dirpath in sorted(SKILLS_DIR.iterdir()):
        if not dirpath.is_dir():
            continue
        skill_file = dirpath / "SKILL.md"
        if not skill_file.exists():
            continue
        nome = dirpath.name
        descricao = ""
        when = []
        raw = ""
        try:
            raw = skill_file.read_text(encoding="utf-8")
        except Exception:
            continue
        # Parse frontmatter YAML simples
        partes = raw.split("---", 2)
        if len(partes) >= 3:
            front = partes[1]
            for linha in front.split("\n"):
                if linha.startswith("description:"):
                    descricao = linha.split(":", 1)[1].strip().strip('"').strip("'")
            # Extract when field (multi-line list)
            in_when = False
            for linha in front.split("\n"):
                if linha.strip().startswith("when:"):
                    in_when = True
                    continue
                if in_when:
                    stripped = linha.strip()
                    if stripped.startswith("- "):
                        when.append(stripped[2:].strip().strip('"'))
                    elif not stripped or not stripped.startswith("- "):
                        in_when = False
        # Se nao achou description no frontmatter, pegar do corpo
        if not descricao:
            for linha in raw.split("\n"):
                linha = linha.strip()
                if linha.startswith("# ") and len(linha) > 2:
                    descricao = linha[2:]
                    break
        # Inferir dominio
        dominio = INFERENCIA_DOMINIO.get(nome, inferir_dominio(descricao, nome))
        # Palavras-chave em portugues
        palavras_chave = PALAVRAS_CHAVE_PT.get(nome, "")
        if not palavras_chave:
            palavras_chave = gerar_palavras_chave(nome, descricao, when)
        skills.append({
            "nome": nome,
            "dominio": dominio,
            "dominio_pt": DOMINIOS_PT.get(dominio, "Outros"),
            "descricao": descricao,
            "palavras_chave": palavras_chave,
            "when": when,
        })
    return skills

def inferir_dominio(descricao, nome):
    d = descricao.lower() + " " + nome.lower()
    if any(w in d for w in ["seguranca", "security", "vulnerabilidade", "auditoria", "codeql", "semgrep"]):
        return "security"
    if any(w in d for w in ["test", "playwright", "e2e", "tdd"]):
        return "testing"
    if any(w in d for w in ["marketing", "seo", "cro", "copy", "anuncio", "ads", "social"]):
        return "marketing"
    if any(w in d for w in ["legal", "contrato", "juridico", "lei", "direito", "advogado"]):
        return "legal"
    if any(w in d for w in ["mobile", "android", "ios", "flutter"]):
        return "mobile"
    if any(w in d for w in ["devops", "docker", "kubernetes", "terraform", "deploy", "ci/cd"]):
        return "devops"
    if any(w in d for w in ["frontend", "web", "css", "react", "ui", "landing page"]):
        return "frontend"
    if any(w in d for w in ["backend", "api", "rest", "graphql", "database", "sql"]):
        return "backend"
    return "utilities"

def gerar_palavras_chave(nome, descricao, when):
    nome_pt = nome.replace("-", " ").replace("_", " ")
    # Extrair da descricao termos significativos
    termos = set()
    for t in re.findall(r'[A-Z][a-z]+(?:\s[A-Z][a-z]+)*', descricao):
        termos.add(t.lower())
    # Extrair do when em portugues
    for w in when:
        if any(p in w.lower() for p in ["usuário", "pede", "quere", "portugu", "brasil"]):
            for t in re.findall(r'\b[a-zà-û]{4,}\b', w.lower()):
                termos.add(t)
    # Combinar
    chaves = list(termos)
    if len(chaves) < 3:
        chaves = [nome_pt[:30]]
    return ", ".join(chaves[:8])

def formatar_genoma(skills, flat=False):
    if flat:
        linhas = ["# SKILL GENOME — Genoma Completo (Lista Plana)\n"]
        linhas.append(f"Total: {len(skills)} skills\n")
        for s in skills:
            linhas.append(f"- **{s['nome']}** [{s['dominio_pt']}]")
            linhas.append(f"  Palavras: {s['palavras_chave']}")
            linhas.append("")
        return "\n".join(linhas)
    else:
        linhas = ["# SKILL GENOME — Genoma Completo por Domínio\n"]
        linhas.append(f"Total: {len(skills)} skills\n")
        # Agrupar por dominio
        grupos = {}
        for s in skills:
            d = s["dominio_pt"]
            grupos.setdefault(d, []).append(s)
        linhas.append("## Índice de Domínios\n")
        for d in sorted(grupos.keys()):
            linhas.append(f"- [{d}](#{d.lower().replace(' ', '-').replace(',', '').replace('(', '').replace(')', '')}) ({len(grupos[d])} skills)")
        linhas.append("")
        for d in sorted(grupos.keys()):
            lista = sorted(grupos[d], key=lambda x: x["nome"])
            linhas.append(f"\n## {d} ({len(lista)} skills)\n")
            for s in lista:
                linhas.append(f"### {s['nome']}")
                linhas.append(f"- **Palavras-chave**: {s['palavras_chave']}")
                linhas.append(f"- **Descrição**: {s['descricao'][:120].strip()}")
                linhas.append("")
        return "\n".join(linhas)

def random_skills(skills, n=3):
    return random.sample(skills, min(n, len(skills)))

def palavras_aleatorias(skills, n=3):
    chaves = []
    for s in random.sample(skills, min(n, len(skills))):
        palavras = [p.strip() for p in s["palavras_chave"].split(",") if p.strip()]
        if palavras:
            chaves.append(random.choice(palavras))
        chaves.append(s["nome"])
    return chaves[:n]

def cross_random(skills):
    dominios = list(set(s["dominio"] for s in skills))
    random.shuffle(dominios)
    selecionados = []
    usados = set()
    for d in dominios[:3]:
        pool = [s for s in skills if s["dominio"] == d and s["nome"] not in usados]
        if not pool:
            continue
        s = random.choice(pool)
        usados.add(s["nome"])
        palavras = [p.strip() for p in s["palavras_chave"].split(",") if p.strip()]
        palavra = random.choice(palavras) if palavras else s["nome"]
        selecionados.append((d, s["nome"], palavra))
    return selecionados

def cross_combo(skills):
    pares = [("legal", "backend"), ("legal", "marketing"), ("esoteric", "marketing"),
             ("backend", "frontend"), ("security", "backend"), ("marketing", "product"),
             ("mobile", "backend"), ("devops", "security"), ("esoteric", "docs"),
             ("ai", "backend"), ("ai", "frontend"), ("legal", "security")]
    par = random.choice(pares)
    d1, d2 = par
    pool1 = [s for s in skills if s["dominio"] == d1]
    pool2 = [s for s in skills if s["dominio"] == d2]
    if not pool1 or not pool2:
        return cross_random(skills)
    s1 = random.choice(pool1)
    s2 = random.choice(pool2)
    p1 = [p.strip() for p in s1["palavras_chave"].split(",") if p.strip()]
    p2 = [p.strip() for p in s2["palavras_chave"].split(",") if p.strip()]
    w1 = random.choice(p1) if p1 else s1["nome"]
    w2 = random.choice(p2) if p2 else s2["nome"]
    return (d1, s1["nome"], w1), (d2, s2["nome"], w2)

def seed_palavra(skills, termo):
    termo = termo.lower().strip()
    resultados = []
    for s in skills:
        chaves = s["palavras_chave"].lower()
        if termo in chaves or termo in s["nome"].lower() or termo in s["descricao"].lower():
            palavras = [p.strip() for p in s["palavras_chave"].split(",") if p.strip()]
            outras = [p for p in palavras if termo not in p.lower()]
            if outras:
                resultados.append((s["nome"], random.choice(outras)))
            if len(resultados) >= 2:
                break
    if len(resultados) < 2:
        extras = random_skills(skills, 2)
        for e in extras:
            palavras = [p.strip() for p in e["palavras_chave"].split(",") if p.strip()]
            if palavras:
                resultados.append((e["nome"], random.choice(palavras)))
    return resultados[:2]

def ponderado_por_projetos(skills, projetos):
    termos = set()
    for p in projetos:
        caminho = pathlib.Path(p)
        if caminho.exists():
            andamento = caminho / "Andamentos KAI.md"
            if andamento.exists():
                try:
                    texto = andamento.read_text(encoding="utf-8")
                    for p_chave in re.findall(r'\b[a-zà-û]{4,}\b', texto.lower()):
                        termos.add(p_chave)
                except Exception:
                    pass
    if not termos:
        return random_skills(skills, 3)
    # Skills que contem algum termo
    match = []
    for s in skills:
        chaves = s["palavras_chave"].lower()
        if any(t in chaves for t in termos):
            match.append(s)
    if len(match) < 3:
        match.extend(random_skills([s for s in skills if s not in match], 3 - len(match)))
    return match[:3]

def capturar_ideia(palavras, nota):
    if not IDEA_BANK_PATH.exists():
        with open(IDEA_BANK_PATH, "w", encoding="utf-8") as f:
            f.write("# 🏦 Banco de Ideias — Gerado pelo Idea Factory\n\n")
    # Ler para achar ultimo ID
    ultimo_id = 0
    try:
        texto = IDEA_BANK_PATH.read_text(encoding="utf-8")
        for m in re.finditer(r'\*\*(IDEA-\d+)\*\*', texto):
            num = int(m.group(1).split("-")[1])
            if num > ultimo_id:
                ultimo_id = num
    except Exception:
        pass
    novo_id = f"IDEA-{ultimo_id + 1:03d}"
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n---\n\n## **{novo_id} — Captura do Idea Factory**\n\n"
    entry += f"**Data**: {agora}\n"
    entry += f"**Palavras**: {palavras}\n"
    entry += f"**Nota**: {nota}\n"
    with open(IDEA_BANK_PATH, "a", encoding="utf-8") as f:
        f.write(entry)
    return novo_id

def modo_captura_interativo():
    print("\n=== CAPTURA DE IDEIA ===")
    palavras = input("\nPalavras que geraram o insight: ").strip()
    if not palavras:
        print("[Cancelado]")
        return
    print("\nDigite sua ideia (nota). Linha em branco encerra:\n")
    linhas_nota = []
    while True:
        linha = input()
        if not linha:
            break
        linhas_nota.append(linha)
    nota = "\n".join(linhas_nota) if linhas_nota else "[sem nota]"
    novo_id = capturar_ideia(palavras, nota)
    print(f"\n✅ Ideia capturada como {novo_id} em {IDEA_BANK_PATH}")

def main():
    parser = argparse.ArgumentParser(description="Idea Factory — Gerador de Insights")
    parser.add_argument("--genome", action="store_true", help="Exibe genoma completo")
    parser.add_argument("--flat", action="store_true", help="Genoma em lista plana (com --genome)")
    parser.add_argument("--cross", choices=["random", "combo"], help="Cruzamento aleatorio de dominios")
    parser.add_argument("--seed", type=str, metavar="TERMO", help="Semente: 1 palavra sua")
    parser.add_argument("--random", action="store_true", help="Palavras aleatorias")
    parser.add_argument("--weighted", type=str, metavar="PROJ1,PROJ2", help="Enviesado por projetos")
    parser.add_argument("--coinflip", action="store_true", help="Aleatorio decide se pondera")
    parser.add_argument("--capture", type=str, nargs="?", const="__interactive__", metavar="PALAVRAS", help="Capturar ideia")
    parser.add_argument("--note", type=str, metavar="TEXTO", help="Nota/descricao da ideia")
    args = parser.parse_args()

    # --- CAPTURE MODE ---
    if args.capture:
        if args.capture == "__interactive__":
            modo_captura_interativo()
            return
        nota = args.note or input("Nota da ideia: ").strip()
        if not nota:
            nota = "[captura rapida]"
        novo_id = capturar_ideia(args.capture, nota)
        print(f"✅ Ideia capturada como {novo_id} em {IDEA_BANK_PATH}")
        return

    # Carregar skills
    skills = carregar_skills()
    if not skills:
        print("[ERRO] Nenhuma skill encontrada.", file=sys.stderr)
        sys.exit(1)

    # --- GENOME MODE ---
    if args.genome:
        output = formatar_genoma(skills, flat=args.flat)
        print(output)
        return

    # --- CROSS MODE ---
    if args.cross:
        if args.cross == "random":
            resultado = cross_random(skills)
            print("\n=== CRUZAMENTO ALEATÓRIO ===\n")
            for d, nome, palavra in resultado:
                print(f"  [{DOMINIOS_PT.get(d, d)}] {nome}: \"{palavra}\"")
            print(f"\n  Palavras: {', '.join(f'\"{p}\"' for _, _, p in resultado)}")
            print("\n  Que insight essas palavras despertam em voce?")
            print("  Use: --capture \"palavras\" --note \"sua ideia\"")
            return
        elif args.cross == "combo":
            r1, r2 = cross_combo(skills)
            print("\n=== CRUZAMENTO COMBO ===\n")
            for d, nome, palavra in [r1, r2]:
                print(f"  [{DOMINIOS_PT.get(d, d)}] {nome}: \"{palavra}\"")
            print(f"\n  Palavras: \"{r1[2]}\" + \"{r2[2]}\"")
            print("\n  Use: --capture \"palavras\" --note \"sua ideia\"")
            return

    # --- SEED MODE ---
    if args.seed:
        resultado = seed_palavra(skills, args.seed)
        print(f'\n=== SEMENTE: "{args.seed}" ===\n')
        for nome, palavra in resultado:
            print(f"  {nome}: \"{palavra}\"")
        todas = [args.seed] + [p for _, p in resultado]
        print(f"\n  Palavras: {', '.join(f'\"{t}\"' for t in todas)}")
        print("\n  Use: --capture \"palavras\" --note \"sua ideia\"")
        return

    # --- RANDOM MODE ---
    if args.random or args.coinflip:
        use_weighted = False
        if args.coinflip:
            use_weighted = random.choice([True, False])
        elif args.weighted:
            use_weighted = True

        if use_weighted and args.weighted:
            projs = [p.strip() for p in args.weighted.split(",")]
            resultado = ponderado_por_projetos(skills, projs)
            print("\n=== ALEATÓRIO PONDERADO (projetos recentes) ===\n")
        else:
            resultado = random_skills(skills, 3)
            print("\n=== ALEATÓRIO PURO ===\n")

        for s in resultado:
            palavras = [p.strip() for p in s["palavras_chave"].split(",") if p.strip()]
            palavra = random.choice(palavras) if palavras else s["nome"]
            print(f"  [{s['dominio_pt']}] {s['nome']}: \"{palavra}\"")
        chaves = []
        for s in resultado:
            palavras = [p.strip() for p in s["palavras_chave"].split(",") if p.strip()]
            chaves.append(random.choice(palavras) if palavras else s["nome"])
        print(f"\n  Palavras: {', '.join(f'\"{c}\"' for c in chaves)}")
        print(f"\n  (dica: --seed \"{chaves[0]}\" para explorar esta palavra)")
        print("  Use: --capture \"palavras\" --note \"sua ideia\"")
        return

    # --- DEFAULT: show help ---
    parser.print_help()

if __name__ == "__main__":
    main()
