import pandas as pd

def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    # Preencher valores ausentes com média
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # ===== NOVO: tratar Pressão Arterial =====
    if "PressaoArterial" in df.columns:
        # Separar valores
        pressao = df["PressaoArterial"].str.split("/", expand=True)

        # Converter para numérico
        sistolica = pd.to_numeric(pressao[0], errors="coerce")
        diastolica = pd.to_numeric(pressao[1], errors="coerce")

        # Preencher valores nulos com mediana
        sistolica.fillna(sistolica.median(), inplace=True)
        diastolica.fillna(diastolica.median(), inplace=True)

        # Reconstituir formato original
        df["PressaoArterial"] = sistolica.astype(int).astype(str) + "/" + diastolica.astype(int).astype(str)

    # Remover idades irreais
    df = df[(df["Idade"] <= 120) & (df["Idade"] >= 0)]

    # Preencher nomes ausentes com "Desconecido"
    if "Nome" in df.columns:
        df["Nome"] = df["Nome"].fillna("Desconhecido")

    # Preencher telefones ausentes com "N/A" e garantir que sejam strings
    if "Telefone" in df.columns:
        df["Telefone"] = df["Telefone"].astype(str)
        df["Telefone"] = df["Telefone"].fillna("N/A")

    return df