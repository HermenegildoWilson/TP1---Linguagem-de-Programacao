import pandas as pd

def calcular_estatisticas(df: pd.DataFrame) -> dict:
    # Selecionar apenas colunas numéricas relevantes
    colunas_analise = ["Idade", "Peso", "Altura", "PressaoArterial", "Colesterol"]
    colunas_validas = [col for col in colunas_analise if col in df.columns]

    df_numerico = df[colunas_validas]

    # Estatísticas base
    estatisticas = df_numerico.describe()

    estatisticasGeral = {
        "Total": estatisticas.loc['count'],
        "Média": estatisticas.loc['mean'],
        "Desvio Padrão": estatisticas.loc['std'],        
        "Minimo": estatisticas.loc['min'],
        "Maximo": estatisticas.loc['max'],
        "1º Quartil": estatisticas.loc['25%'],
        "Mediana": estatisticas.loc['50%'],
        "3º Quartil": estatisticas.loc['75%'],
        "Moda": df_numerico.mode().iloc[0] if not df_numerico.mode().empty else None,
    }    

    return estatisticasGeral


def imprimirEstatisticasGeral(estatisticasGeral: dict):
    for stat, values in estatisticasGeral.items():
        print(f"{stat.upper():=^42}")
        
        # Converter para dicionário para evitar Name e dtype
        valores_dict = values.to_dict() if hasattr(values, "to_dict") else values
        
        for coluna, valor in valores_dict.items():
            print(f"{coluna:<35} {round(valor, 2) if isinstance(valor, (int, float)) else valor}")
        
        print("\n")