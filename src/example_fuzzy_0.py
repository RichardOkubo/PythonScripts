import pandas as pd

gerador = (
    (design, potencia, economia, preco, espaco)
    for design in ["feio", "razoável", "belo"]
    for potencia in ["baixa", "média", "alta"]
    for economia in ["baixa", "média", "alta"]
    for preco in ["elevado", "coerente", "barato"]
    for espaco in ["apertado", "médio", "espaçoso"]
)

df = pd.DataFrame(
    list(gerador), columns=["design", "potência", "economia", "preço", "espaço"]
)

df.to_csv("dados.csv", index=False)
