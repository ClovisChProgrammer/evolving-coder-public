# Feedback em Operacoes Longas

Silencio >5min deixa o SPA sem saber se o KAI travou. Regras:

1. **Antes** de comando com duracao esperada >2min: avisar ("isso pode levar ~N min").
2. **Ao concluir**: reportar duracao real quando relevante.
3. Operacoes previsivelmente longas (>5min): segmentar em passos menores com marcadores [✅ n/N] entre eles.
4. Complemento visual: sprite KAI emite bolha "ainda trabalhando ⏳ (N min)" a cada 90s apos 5min no mesmo estado (implementado no kai_sprite.py + campo since do payload).
