import pandas as pd

def carregar_dados(caminho: str) -> None:
    df = pd.read_csv(caminho)    
    return df
