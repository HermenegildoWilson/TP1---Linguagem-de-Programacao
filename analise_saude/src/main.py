from load_data import carregar_dados
from clean_data import limpar_dados
from visualization import plot_histograma, salvar_histograma, plot_heatmap
from correlation import calcular_correlacao, imprimir_correlacao
from stats import calcular_estatisticas, imprimirEstatisticasGeral

def main():
    caminhoArq = './data/pacientes.csv'
    caminhoSaida = './output'

    df = carregar_dados(caminhoArq)
    df = limpar_dados(df)


    # Plotar
    # plot_histograma(df, "Idade")
    # salvar
    # salvar_histograma(df, "Idade", caminhoSaida)


    # correlacao = calcular_correlacao(df)
    # imprimir_correlacao(correlacao)
    # plot_heatmap(correlacao)


    estatisticasGeral = calcular_estatisticas(df)
    imprimirEstatisticasGeral(estatisticasGeral)

if __name__ == "__main__":
    main()