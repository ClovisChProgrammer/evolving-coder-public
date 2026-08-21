# Mandala Studio v2 — Manual / Manual / Manual

## English

### What is Mandala Studio v2?

A comprehensive sacred geometry generator for meditation and self-discovery. Create intricate, multi-layered procedural SVG mandalas with kaleidoscope effects, 12 color palettes with HSL controls, a digital painting module, and an animation engine with meditation sync. Includes fullscreen meditation mode with binaural beats (Delta→Gamma), pause/resume, and breathing guide.

### How to Use

1. Open `mandala-studio.html` in any modern browser
2. Use the **sidebar tabs** (Structure / Pattern / Colors / Modes / Animation) to customize
3. The mandala generates in real-time

### 12 Presets

| Preset | Description |
|--------|-------------|
| 🕉️ Tibetan | 8-fold lotus, jewel palette, deep intensity |
| 🪷 Lotus | 12-fold layered lotus, sunset palette |
| ⭐ Star | Triangular patterns, warm palette |
| 🍀 Celtic | Interwoven weave, forest palette, earth intensity |
| 🔮 Kaleidoscope | 16-fold mirror segments, rainbow, phase offset |
| 🌸 Flower | Petals, pastel palette |
| 🔷 Geometric | Diamonds, monochrome, clean |
| 🌊 Ocean | Waves, ocean palette, deep intensity |
| 🔥 Flame | Organic flame shapes, sunset palette |
| 💜 Neon | Scales, neon palette, kaleidoscope mode |
| ⚪ Minimal | Simple dots, monochrome |
| ✡️ Sacred | Intricate mix + Om center, jewel palette |

### 12 Pattern Types

| Pattern | Description |
|---------|-------------|
| Petals | Layered teardrops with veins and tip dots |
| Lotus | 3-layer overlapping petals with phase offsets |
| Diamonds | Nested diamonds with inner cutouts |
| Dots | Concentric circles with micro-dot rings |
| Arcs | Interlocking arcs with connection dots |
| Triangles | Pointed shapes with median lines |
| Waves | Dual sine waves with crest dots |
| Zigzag | Sharp alternating patterns |
| Weave | Celtic interlace with over/under strands |
| Flame | Organic flame shapes with inner layers |
| Scales | Overlapping scale patterns |
| Intricate | Combined arc + diamond + dots per element |

### 6 Center Patterns

| Pattern | Description |
|---------|-------------|
| Bindu | Traditional origin point with concentric rings |
| Flower | 8-petal flower with inner details |
| Star | 6-pointed star with dots |
| Spiral | Growing spiral inward |
| Lotus center | Multi-layer lotus at center |
| Om | Sacred ॐ symbol |

### Color System

**12 Palettes**: Vivid, Pastel, Warm, Cool, Earth, Jewel, Sunset, Ocean, Forest, Neon, Monochrome, Rainbow

**HSL Controls**:
- Hue Rotation (0–360°): Shifts color progression between rings
- Saturation (0–100%): Color intensity
- Lightness (20–80%): Brightness

**6 Intensity Modes**: Vivid, Pastel, Muted, Deep, Neon, Earth

**Custom Blend**: Pick two colors to create a custom gradient palette

### Kaleidoscope Mode

- **Mirror segments**: Number of reflection axes (2–16)
- **Phase offset**: Angular offset between rings (0–90°)
- **Variation**: Random variation within symmetry (0–50%)

### Digital Painting Module

1. Enable **Coloring / Paint mode** in Modes tab
2. Canvas overlay appears over the mandala
3. Click anywhere to flood-fill that region
4. 24-color palette + custom color picker
5. Undo/Redo support (20 steps)
6. Click **Done** to exit painting

### Decorative Borders

Between each ring, decorative bands add complexity:
- **Dots**: Repeating dot patterns
- **Radial lines**: Thin lines radiating outward
- **Mini diamonds**: Small diamond shapes
- **None**: No borders

### Complexity Control

Levels 1–5 add internal detail to each element:
1. Base shape only
2. + Second layer
3. + Inner veins/details
4. + Tip dots/connection points
5. + Full detail

### Animation Tab

The **Animation** tab provides a complete animation engine for your mandala:

**Passive Animation:**
- **Rotate** left, right, or off — with adjustable speed (0–5x)
- **Pulse/Zoom** — breathing zoom effect with intensity and speed controls

**Color Wave:**
- Colors cycle from center→out, out→center, or random
- Adjustable speed and intensity
- Uses CSS hue-rotate for GPU-accelerated performance

**Inverse Mode:**
- Colors and shapes animate in different directions
- Colors: center→out or out→center
- Shapes: center→out or out→center
- Creates mesmerizing counter-wave effects

**Sync Meditation:**
- Links rotation speed to binaural beat frequency
- Hz multiplier (0.1–5.0x): rotation speed × multiplier = binaural Hz
- E.g.: 1.0x rotation × 1.5 multiplier = 1.5 Hz (Theta)
- Works with meditation overlay — binaural audio follows your rotation speed

**Full Random:**
- Randomizes both mandala pattern and all animation settings
- Includes random frame shape selection
- Immediately starts playing the result

### Frame Shapes

Choose the outer shape of your mandala:
- **Circle** (default) — traditional round mandala
- **Square** — angular, geometric feel
- **Diamond** — rotated square, dynamic
- **Pentagon** — 5-sided sacred geometry
- **Hexagon** — honeycomb pattern, balanced
- **Octagon** — 8-sided, bridges circle and square

### Meditation Mode

Click **Meditate** to enter a fullscreen meditation experience:

**Overlay:**
- Fullscreen dark overlay with mandala centered
- Breathing guide animation (4-7-8 pattern)
- Digital timer (5 minutes)
- Pause/Resume button

**Binaural Audio:**
- Beat frequency: 0.1–40 Hz (Delta → Gamma)
- Base tone: 80–600 Hz
- Volume: 0–50%
- Beat type labels (Delta → Gamma) update in real-time
- When Sync Meditation is ON in Animation tab: Hz is calculated from rotation speed × multiplier

**Controls:**
- Beat Frequency (ΔHz): difference between left/right ears
- Base Frequency: carrier tone for both ears
- Volume: overall audio level
- Pause/Resume: stops timer + audio + animation

---

## Português (Brasil)

### O que é Mandala Studio v2?

Um gerador abrangente de geometria sagrada para meditação e autoconhecimento. Crie mandalas SVG procedurais intrincadas e multicamadas com efeitos caleidoscópio, 12 paletas de cores com controles HSL e um módulo de pintura digital. Inclui modo meditação fullscreen com batimentos binaurais (Delta→Gamma), pausar/continuar e guia respiratório.

### Como Usar

1. Abra `mandala-studio.html` em qualquer navegador moderno
2. Use as **abas da barra lateral** (Structure / Pattern / Colors / Modes)
3. A mandala gera em tempo real

### 12 Presets

| Preset | Descrição |
|--------|-----------|
| 🕉️ Tibetan | Lótus 8x, paleta jewel, intensidade deep |
| 🪷 Lotus | Lótus multicamada 12x, paleta sunset |
| ⭐ Star | Padrões triangulares, paleta warm |
| 🍀 Celtic | Traçado entrelaçado, paleta forest, earth |
| 🔮 Kaleidoscope | Espelhamento 16x, rainbow, phase offset |
| 🌸 Flower | Pétalas, paleta pastel |
| 🔷 Geometric | Diamantes, monocromático |
| 🌊 Ocean | Ondas, paleta ocean, deep |
| 🔥 Flame | Chamas orgânicas, paleta sunset |
| 💜 Neon | Escamas, paleta neon, caleidoscópio |
| ⚪ Minimal | Pontos simples, monocromático |
| ✡️ Sacred | Mix intrincado + centro Om, paleta jewel |

### 12 Tipos de Padrão

| Padrão | Descrição |
|--------|-----------|
| Petals | Gotas multicamada com veins e pontos |
| Lotus | 3 camadas de pétalas sobrepostas |
| Diamonds | Diamantes aninhados com cortes internos |
| Dots | Círculos concêntricos com micro-dots |
| Arcs | Arcos entrelaçados com pontos de conexão |
| Triangles | Formas pontiagudas com linhas medianas |
| Waves | Ondas duplas com pontos nas cristas |
| Zigzag | Padrões alternados afiados |
| Weave | Traçado celta com fios sobre/sob |
| Flame | Chamas orgânicas com camadas internas |
| Scales | Padrões de escamas sobrepostas |
| Intricate | Arc + diamante + dots combinados |

### 6 Padrões Centrais

| Padrão | Descrição |
|--------|-----------|
| Bindu | Ponto de origem com anéis concêntricos |
| Flower | Flor de 8 pétalas com detalhes internos |
| Star | Estrela de 6 pontas com pontos |
| Spiral | Espiral crescendo para dentro |
| Lotus center | Lótus multicamada no centro |
| Om | Símbolo sagrado ॐ |

### Sistema de Cores

**12 Paletas**: Vivid, Pastel, Warm, Cool, Earth, Jewel, Sunset, Ocean, Forest, Neon, Monochrome, Rainbow

**Controles HSL**:
- Rotação de Hue (0–360°): Altera progressão de cor entre anéis
- Saturação (0–100%): Intensidade da cor
- Luminosidade (20–80%): Brilho

**6 Modos de Intensidade**: Vivid, Pastel, Muted, Deep, Neon, Earth

**Blend Personalizado**: Escolha duas cores para criar paleta gradiente

### Modo Caleidoscópio

- **Segmentos espelho**: Número de eixos de reflexão (2–16)
- **Phase offset**: Offset angular entre anéis (0–90°)
- **Variação**: Variação aleatória dentro da simetria (0–50%)

### Módulo de Pintura Digital

1. Ative **Coloring / Paint mode** na aba Modes
2. Canvas sobreposto aparece sobre a mandala
3. Clique em qualquer lugar para preencher aquela região
4. Paleta de 24 cores + seletor personalizado
5. Undo/Redo (20 passos)
6. Clique em **Done** para sair

### Bandas Decorativas

Entre cada anél, bandas adicionam complexidade:
- **Dots**: Padrões de pontos repetidos
- **Radial lines**: Linhas finas radiais
- **Mini diamonds**: Formas de diamante pequenas
- **None**: Sem bordas

### Controle de Complexidade

Níveis 1–5 adicionam detalhes internos a cada elemento:
1. Forma base apenas
2. + Segunda camada
3. + Veins/detalhes internos
4. + Pontos de conexão
5. + Detalhe completo

### Aba de Animação

A aba **Animation** fornece um motor completo de animação para sua mandala:

**Animação Passiva:**
- **Girar** para direita, esquerda ou desligado — com velocidade ajustável (0–5x)
- **Pulsar/Zoom** — efeito de zoom respiratório com controles de intensidade e velocidade

**Onda de Cores:**
- Cores ciclam de centro→fora, fora→centro ou aleatório
- Velocidade e intensidade ajustáveis
- Usa CSS hue-rotate para performance acelerada por GPU

**Modo Inverso:**
- Cores e formas animam em direções diferentes
- Cores: centro→fora ou fora→centro
- Formas: centro→fora ou fora→centro
- Cria efeitos de onda contra-fluxo hipnóticos

**Sincronizar Meditação:**
- Vincula velocidade de rotação à frequência dos batimentos binaurais
- Multiplicador Hz (0.1–5.0x): velocidade × multiplicador = Hz binaural
- Ex: rotação 1.0x × mult 1.5 = 1.5 Hz (Theta)
- Funciona com overlay de meditação — áudio binaural acompanha sua rotação

**Aleatório Completo:**
- Randomiza padrão da mandala e todas as configurações de animação
- Inclui seleção aleatória de formato do frame
- Inicia reprodução imediatamente

### Formatos de Frame

Escolha a forma externa da sua mandala:
- **Círculo** (padrão) — mandala tradicional redonda
- **Quadrado** — sensação geométrica angular
- **Diamante** — quadrado rotacionado, dinâmico
- **Pentágono** — geometria sagrada de 5 lados
- **Hexágono** — padrão colmeia, equilibrado
- **Octógono** — 8 lados, ponte entre círculo e quadrado

### Modo Meditação

Clique em **Meditate** para entrar em uma experiência de meditação fullscreen:

**Overlay:**
- Overlay fullscreen escuro com mandala centralizada
- Animação de guia respiratório (padrão 4-7-8)
- Timer digital (5 minutos)
- Botão Pausar/Continuar

**Áudio Binaural:**
- Frequência de batimento: 0.1–40 Hz (Delta → Gamma)
- Tom base: 80–600 Hz
- Volume: 0–50%
- Labels de tipo de onda (Delta → Gamma) atualizam em tempo real
- Quando Sync Meditation está ligado na aba Animation: Hz é calculada da velocidade de rotação × multiplicador

**Controles:**
- Frequência de Batimento (ΔHz): diferença entre ouvidos esquerdo/direito
- Frequência Base: tom portador para ambos os ouvidos
- Volume: nível geral do áudio
- Pausar/Continuar: para timer + áudio + animação

---

## Español

### ¿Qué es Mandala Studio v2?

Un generador integral de geometría sagrada para meditación y autodescubrimiento. Crea mandalas SVG procedurales intrincados y multicapa con efectos caleidoscopio, 12 paletas de colores con controles HSL y un módulo de pintura digital. Incluye modo meditación fullscreen con batidos bináuricos (Delta→Gamma), pausar/reanudar y guía respiratoria.

### Cómo Usar

1. Abre `mandala-studio.html` en cualquier navegador moderno
2. Usa las **pestañas** (Structure / Pattern / Colors / Modes)
3. La mandala se genera en tiempo real

### 12 Presets

| Preset | Descripción |
|--------|-------------|
| 🕉️ Tibetan | Loto 8x, paleta jewel, intensidad deep |
| 🪷 Lotus | Loto multicapa 12x, paleta sunset |
| ⭐ Star | Patrones triangulares, paleta warm |
| 🍀 Celtic | Trabajo entrelazado, paleta forest |
| 🔮 Kaleidoscope | Espejo 16x, rainbow, phase offset |
| 🌸 Flower | Pétalos, paleta pastel |
| 🔷 Geometric | Diamantes, monocromático |
| 🌊 Ocean | Ondas, paleta ocean |
| 🔥 Flame | Llamas orgánicas, paleta sunset |
| 💜 Neon | Escamas, paleta neon |
| ⚪ Minimal | Puntos simples, monocromático |
| ✡️ Sacred | Mix intrincado + centro Om |

### 12 Tipos de Patrón

| Patrón | Descripción |
|--------|-------------|
| Petals | Gotas multicapa con venas y puntos |
| Lotus | 3 capas de pétalos superpuestos |
| Diamonds | Diamantes anidados con cortes internos |
| Dots | Círculos concéntricos con micro-dots |
| Arcs | Arcos entrelazados con puntos de conexión |
| Triangles | Formas puntiagudas con líneas medianas |
| Waves | Ondas duales con puntos en crestas |
| Zigzag | Patrones alternados afilados |
| Weave | Trabajo celta con hilos sobre/sotto |
| Flame | Llamas orgánicas con capas internas |
| Scales | Patrones de escamas superpuestas |
| Intricate | Arco + diamante + dots combinados |

### 6 Patrones Centrales

| Patrón | Descripción |
|--------|-------------|
| Bindu | Punto de origen con anillos concéntricos |
| Flower | Flor de 8 pétalos con detalles internos |
| Star | Estrella de 6 puntas con puntos |
| Spiral | Espiral creciente hacia adentro |
| Lotus center | Loto multicapa en el centro |
| Om | Símbolo sagrado ॐ |

### Sistema de Colores

**12 Paletas**: Vivid, Pastel, Warm, Cool, Earth, Jewel, Sunset, Ocean, Forest, Neon, Monochrome, Rainbow

**Controles HSL**:
- Rotación de Hue (0–360°): Cambia la progresión de color entre anillos
- Saturación (0–100%): Intensidad del color
- Luminosidad (20–80%): Brillo

**6 Modos de Intensidad**: Vivid, Pastel, Muted, Deep, Neon, Earth

### Modo Caleidoscopio

- **Segmentos espejo**: Número de ejes de reflexión (2–16)
- **Phase offset**: Offset angular entre anillos (0–90°)
- **Variación**: Variación aleatoria dentro de la simetría (0–50%)

### Módulo de Pintura Digital

1. Activa **Coloring / Paint mode** en la pestaña Modes
2. Canvas superpuesto aparece sobre la mandala
3. Haz clic en cualquier lugar para rellenar esa región
4. Paleta de 24 colores + selector personalizado
5. Undo/Redo (20 pasos)
6. Haz clic en **Done** para salir

### Bandas Decorativas

Entre cada anillo, bandas añaden complejidad:
- **Dots**: Patrones de puntos repetidos
- **Radial lines**: Líneas finas radiales
- **Mini diamonds**: Formas de diamante pequeñas
- **None**: Sin bordas

### Control de Complejidad

Niveles 1–5 añaden detalles internos a cada elemento:
1. Forma base solamente
2. + Segunda capa
3. + Venas/detalles internos
4. + Puntos de conexión
5. + Detalle completo

### Pestaña de Animación

La pestaña **Animation** proporciona un motor completo de animación para tu mandala:

**Animación Pasiva:**
- **Rotar** a la derecha, izquierda o apagado — con velocidad ajustable (0–5x)
- **Pulsar/Zoom** — efecto de zoom respiratorio con controles de intensidad y velocidad

**Ola de Colores:**
- Los colores ciclan de centro→fuera, fuera→centro o aleatorio
- Velocidad e intensidad ajustables
- Usa CSS hue-rotate para rendimiento acelerado por GPU

**Modo Inverso:**
- Colores y formas animan en direcciones diferentes
- Colores: centro→fuera o fuera→centro
- Formas: centro→fuera o fuera→centro
- Crea efectos de onda contra-flujo hipnóticos

**Sincronizar Meditación:**
- Vincula la velocidad de rotación a la frecuencia de los batidos bináuricos
- Multiplicador Hz (0.1–5.0x): velocidad × multiplicador = Hz bináurico
- Ej: rotación 1.0x × mult 1.5 = 1.5 Hz (Theta)
- Funciona con overlay de meditación — el audio bináurico sigue tu velocidad de rotación

**Aleatorio Completo:**
- Aleatoriza el patrón de la mandala y todas las configuraciones de animación
- Incluye selección aleatoria de forma del marco
- Inicia la reproducción inmediatamente

### Formas de Marco

Elige la forma exterior de tu mandala:
- **Círculo** (predeterminado) — mandala tradicional redonda
- **Cuadrado** — sensación geométrica angular
- **Diamante** — cuadrado rotacionado, dinámico
- **Pentágono** — geometría sagrada de 5 lados
- **Hexágono** — patrón de panal, equilibrado
- **Octágono** — 8 lados, puente entre círculo y cuadrado

### Modo Meditación

Haz clic en **Meditate** para entrar en una experiencia de meditación fullscreen:

**Overlay:**
- Overlay fullscreen oscuro con mandala centrada
- Animación de guía respiratoria (patrón 4-7-8)
- Temporizador digital (5 minutos)
- Botón Pausar/Reanudar

**Audio Bináurico:**
- Frecuencia de batido: 0.1–40 Hz (Delta → Gamma)
- Tono base: 80–600 Hz
- Volumen: 0–50%
- Etiquetas de tipo de onda (Delta → Gamma) se actualizan en tiempo real
- Cuando Sincronizar Meditación está activo en pestaña Animation: Hz se calcula de velocidad de rotación × multiplicador

**Controles:**
- Frecuencia de Batido (ΔHz): diferencia entre oídos izquierdo/derecho
- Frecuencia Base: tono portador para ambos oídos
- Volumen: nivel general del audio
- Pausar/Reanudar: detiene temporizador + audio + animación

---

*Mandala Studio v2 by Kai (SPD) — August 2026 (updated)*
*Mandala Studio v2 por Kai (SPD) — Agosto 2026 (actualizado)*
*Mandala Studio v2 por Kai (SPD) — Agosto 2026 (atualizado)*
