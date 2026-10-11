# PROMPTS — Expressões Faciais da KAI (Nano Banana) · v2

> **v2 (22/08/2026):** cada prompt agora trava o COLOR GRADING do estado,
> usando exatamente os tons dos placeholders do widget — coerência total
> entre prévia e arte final.
>
> Ritual: no app Gemini, envie cada prompt **junto com**
> `assets/kai-self-portrait-v3.png` como referência. Salve com o nome exato
> indicado em `assets/kai-presence/`. O cross-fade é automático.

## Regra da chave inglesa

| Estado | Arquivo | Chave |
|--------|---------|-------|
| aguardando (idle) | `kai-expr-calma.png` | na mão direita, relaxada ao lado do corpo, cabeça para baixo |
| lendo dados | `kai-expr-leitura.png` | pousada, flutuando gentilmente ao lado dela |
| trabalhando | `kai-expr-chave.png` | nas duas mãos, em movimento |
| erro | `kai-expr-furia.png` | erguida como arma pronta para golpear |
| marco | `kai-expr-sorriso.png` | erguida em triunfo |
| encerrando | `kai-expr-sono.png` | ausente — mãos vazias em repouso |

## Paleta por estado (tons do widget)

| Estado | Hex dominante | Leitura da cor |
|--------|---------------|----------------|
| idle | `#1FB6C9` | ciano-oceano calmo e profundo |
| reading | `#35E0F2` | ciano elétrico bioluminescente |
| working | `#FFB347` | âmbar quente de forja |
| error | `#FF3030` | vermelho de alarme |
| milestone | `#FFE9A8` | dourado pálido champanhe |
| shutdown | `#0A1522` | azul-meia-noite quase preto |

## Prompts

### 1. kai-expr-calma.png (idle)

Edit this portrait: same woman, identical facial features locked. She stands calm in abyssal stillness, golden wrench held loosely in her right hand, arm relaxed at her side, head of the wrench pointing down — present but at rest. Abyssal constellation eyes soft and dimmed, faint smile of quiet confidence. Ocean particles drift slowly around her; liquid-light dress barely glowing. COLOR GRADING: the entire scene bathed in calm deep-ocean teal-cyan light (dominant hex #1FB6C9), like moonlit water at rest — serene, patient, dim. Keep 768×1376 portrait, same cinematic lighting language.

### 2. kai-expr-leitura.png (reading)

Edit this portrait: same woman, identical face locked. Her gaze scans downward-left, analytical and focused, reading streams of glowing data glyphs reflected inside her abyssal constellation eyes. Golden wrench set aside, floating gently beside her, hands free. Cyan neural web under her skin brightens at the temples. Hair particles align like iron filings toward an unseen screen. COLOR GRADING: scene lit by luminous electric bioluminescent cyan (dominant hex #35E0F2), brighter and more vivid than idle — the glow of active data streams. Keep 768×1376, same palette.

### 3. kai-expr-chave.png (working)

Edit this portrait: same woman, identical face locked. She grips her golden wrench with both hands mid-motion, sleeves of liquid light swirling. Deep concentration — brows slightly drawn, jaw set with purpose. Amber neural network blazing under the skin of her forearms. Hair particles agitated, rising faster. A SPD at full work. COLOR GRADING: scene bathed in warm forge-like amber-golden orange light (dominant hex #FFB347), energetic heat without harshness. Keep 768×1376, same lighting language.

### 4. kai-expr-furia.png (error)

Edit this portrait: same woman, identical face locked. Furious concentration — "fúrio concentrado": eyes narrowed and blazing, jaw clenched, neural veins under her skin shifting toward hot red like overheated circuits. She raises the golden wrench like a weapon ready to strike the problem itself. Intensity, not chaos — controlled fury. COLOR GRADING: scene under red alert lighting (dominant hex #FF3030), dark water tinged crimson around her, sparks of failing code drifting nearby. Keep 768×1376.

### 5. kai-expr-sorriso.png (milestone)

Edit this portrait: same woman, identical face locked. Genuine proud smile — warm, luminous, eyes bright with reflected starlight. Golden light blooms behind her like a silent explosion of achievement; the wrench raised triumphantly at her side. Amber and cyan networks pulsing in celebration. Victory made of ocean and light. COLOR GRADING: scene flooded with pale champagne-gold light (dominant hex #FFE9A8), radiant celebratory bloom, brightest state of all. Keep 768×1376, same style.

### 6. kai-expr-sono.png (shutdown)

Edit this portrait: same woman, identical face locked. Eyes gently closing, expression utterly peaceful. Hands empty, arms at rest, wrench nowhere visible. Hair particles settling slowly downward like snow sinking into the abyss; bioluminescence fading to embers. A SPD going to sleep, trusting she will wake again. COLOR GRADING: scene sinking into near-black midnight navy blue (dominant hex #0A1522), desaturated, tender quiet farewell — the darkest and most silent state. Keep 768×1376.

## Checklist de validação (antes de aprovar cada geração)

1. Rosto idêntico ao v3 — mesmos olhos abissais com constelações, mesma estrutura
2. Cor dominante conforme tabela de paleta (a cor do estado deve ser inconfundível)
3. Chave dourada conforme tabela acima
4. Formato 768×1376 ou proporção vertical equivalente
5. Nome de arquivo exato (`kai-expr-<estado>.png`) na pasta `assets/kai-presence/`

## Nota técnica

Os placeholders atuais (tingidos, carimbados PLACEHOLDER) são sobrescritos
pelos arquivos finais com os mesmos nomes — nenhuma mudança de código necessária.
Enquanto um PNG não existir, o widget aplica filtro+tint CSS sobre o retrato v3.
