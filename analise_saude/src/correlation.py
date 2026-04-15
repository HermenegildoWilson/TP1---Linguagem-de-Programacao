import pandas as pd

def calcular_correlacao(df: pd.DataFrame) -> pd.DataFrame:
    colunas_analise = ["Idade", "Peso", "Altura", "Colesterol"]
    colunas_validas = [col for col in colunas_analise if col in df.columns]

    df_numerico = df[colunas_validas]

    correlacao = df_numerico.corr()

    return correlacao

"""
Escala de interpretação da correlação:
| Valor | Interpretação             |
| ----- | ------------------------- |
| +1    | Correlação forte positiva |
| 0     | Sem relação               |
| -1    | Correlação forte negativa |
"""


def imprimir_correlacao(correlacao):
    print(f"{'MATRIZ DE CORRELAÇÃO':=^50}")
    
    for coluna in correlacao.columns:
        print(f"\n{coluna}:")
        for index, valor in correlacao[coluna].items():
            print(f"  {index:<20} {round(valor, 2)}")