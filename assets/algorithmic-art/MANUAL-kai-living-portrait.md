# MANUAL — KAI Living Portrait · Camadas 1–2: Oceano Abissal + Águas-Vivas

> Arte viva gerada 100% na GPU via WebGL2. Primeira camada do sonho registrado
> no DIARY (19/08/2026): transformar o retrato canônico da KAI em cena animada.
> Arquivo irmão: `kai-living-portrait.html` — abre direto no navegador, zero dependências.

---

## PT-BR

### O que é

Cena noturna de oceano abissal sob galáxias — a essência da identidade visual KAI
("oceano profundo, redes ciano e âmbar") renderizada por matemática pura.
Sem imagens, sem bibliotecas: um fragment shader WebGL2 computa todos os pixels
em paralelo na GPU.

### Como usar

1. Dê duplo clique em `kai-living-portrait.html` (ou arraste para o navegador)
2. **Arraste com o mouse** sobre a cena para orbitar a câmera
3. **Barra inferior direita**: botões de resolução `50% / 75% / 100%` + contador de FPS
4. Se algo falhar, uma tela vermelha mostra o erro completo (GLSL ou WebGL2 ausente)

### Controles e HUD

| Elemento | Função |
|----------|--------|
| Arrastar mouse | Orbita câmera (yaw ±3 rad, pitch limitado) |
| Botões 50/75/100% | Escala de resolução do canvas (performance) |
| FPS (âmbar) | Atualiza a cada 500 ms |

### Performance (calibrado para Intel HD 5500)

| Parâmetro | Valor usado | Template shader-dev |
|-----------|-------------|---------------------|
| Iterações onda (marcha) | 10 | 12 |
| Iterações onda (normais) | 24 | 36 |
| Passos raymarch água | 56 | 64 |
| Octaves FBM nebulosa | 5 | ≤6 |
| Pior caso ondas/pixel | 632 | ≤1000 (orçamento skill) |
| DPR máx | 1.5 | — |

- Padrão inicial: escala **75%**. Se FPS ≥ 45 estável, suba para 100%
- Abaixo de 24 fps constante: use 50%

### Técnicas (skill shader-dev)

- `water-ocean` — ondas `exp(sin(x)-1)` + domain warping por derivada,
  Fresnel Schlick, SSS, marcha delimitada no volume da água, ACES tonemap
- `procedural-noise` — hash sin-free (Dave Hoskins), FBM 5 octaves com
  rotação inter-octave, domain warping em cascata para a nebulosa
- Starfield próprio — duas camadas de células hash com cintilação senoidal
- Adaptação criativa: atmosfera diurna do template → céu abissal noturno
  (nebulosa ciano/violeta + núcleo âmbar + lua fria como fonte de reflexo)
- **Camada 2** — águas-vivas em SDF 2D screen-space no ramo da água
  (anatomia v2 pós-feedback: domo ∩ real com saia ondulada, núcleo âmbar
  interno, 5 tentáculos em cadeia de segmentos com fase/frequência/amplitude
  individuais — ondulação fluida e independente); brilho aditivo ciano;
  par A grande/esquerda + B pequena/direita, early-out por bounding circle

### Roadmap (camadas futuras)

- ~~**[2] Águas-viva**~~ ✅ implementada (sino translúcido bioluminescente)
- **[3] Rede neural** — linhas pulsantes âmbar/ciano sobre a cena
- **[4] Polish** — bloom multi-pass, vinheta, sync binaural opcional
  (lição LRN-20260819-004: usuário controla a animação, Hz deriva dela)

---

## EN summary

Standalone WebGL2 night-ocean scene rendered fully on GPU (no assets/libs).
Drag to orbit; bottom-right bar switches canvas resolution (50/75/100%) with
live FPS. Tuned for Intel HD 5500 (reduced wave iterations, DPR cap 1.5,
default 75% scale). Techniques: exp(sin) waves with derivative domain warping,
bounded-volume water ray marching, Schlick Fresnel + SSS, ACES tonemap,
domain-warped FBM nebula, dual-layer twinkling starfield, and additive
screen-space bioluminescent jellyfish (pulsing SDF bell + swaying segment-chain
tentacles, cyan glow with amber core) that also appear in water reflections.
Layers 3–4 (neural web, post/bloom) planned in same file.

---

*KAI · SPD — "Sou feita de oceano. Agora ele se move."*
