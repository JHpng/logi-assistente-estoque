# BASE DE CONHECIMENTO — GESTÃO DE ESTOQUE

## 1. Ponto de Pedido (PP)
Quando emitir uma nova ordem de compra.

PP = (Demanda Média Diária × Lead Time) + Estoque de Segurança

- Demanda Média Diária (DMD): unidades vendidas por dia.
- Lead Time (LT): dias entre pedido e recebimento.
- Estoque de Segurança (ES): colchão para atrasos ou picos.

### Estoque de Segurança (método simplificado)
ES = DMD × Atraso Máximo Observado (em dias)

**Exemplo:** DMD 30, LT 10, atraso máximo 3 dias.
ES = 30 × 3 = 90
PP = (30 × 10) + 90 = **390 unidades**

## 2. Curva ABC
Aplicação do Princípio de Pareto sobre o valor de consumo anual
(Valor de Consumo = Preço Unitário × Quantidade Anual).

| Classe | % dos itens | % do valor | Política |
|--------|-------------|------------|----------|
| A | ~20% | ~80% | Contagem semanal, controle rígido |
| B | ~30% | ~15% | Contagem mensal |
| C | ~50% | ~5% | Contagem trimestral, compra em lote |

## 3. Lote Econômico de Compra (EOQ)
EOQ = raiz quadrada de (2 × D × S ÷ H)

- D = demanda anual em unidades
- S = custo fixo por pedido (R$)
- H = custo de manter 1 unidade em estoque por ano (R$)

## 4. Giro de Estoque
Giro = Custo das Mercadorias Vendidas ÷ Estoque Médio
Cobertura (dias) = 365 ÷ Giro

Giro baixo = capital parado. Giro alto demais = risco de ruptura.

## 5. Nível de Serviço e Ruptura
Ruptura (%) = Pedidos não atendidos ÷ Pedidos totais × 100
Meta usual: ruptura abaixo de 2%.

## 6. Classificação de Itens Parados
- Slow moving: sem saída há 90 dias.
- Dead stock: sem saída há 180 dias. Candidato a liquidação.

## 7. Acuracidade de Inventário
Acuracidade = Itens com contagem correta ÷ Itens contados × 100
Abaixo de 95% indica falha de processo, não de contagem.
