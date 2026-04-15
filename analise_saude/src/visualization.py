import matplotlib.pyplot as plt
import pandas as pd

def plot_histograma(df: pd.DataFrame, coluna: str) -> None:
    plt.figure()

    df[coluna].hist(bins=10)

    plt.title(f"Distribuição de {coluna}")
    plt.xlabel(coluna)
    plt.ylabel("Frequência")

    plt.grid(False)
    plt.show()


def salvar_histograma(df, coluna, caminho_saida):
    plt.figure()

    df[coluna].hist(bins=10)

    plt.title(f"Distribuição de {coluna}")
    plt.xlabel(coluna)
    plt.ylabel("Frequência")

    plt.savefig(f"{caminho_saida}/{coluna}.png")
    plt.close()


def plot_heatmap(correlacao):
    plt.imshow(correlacao, cmap='coolwarm', interpolation='nearest')
    plt.colorbar()

    plt.xticks(range(len(correlacao.columns)), correlacao.columns, rotation=45)
    plt.yticks(range(len(correlacao.columns)), correlacao.columns)

    plt.title("Matriz de Correlação")
    plt.show()