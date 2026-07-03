import pandas as pd
from dados import busca_dados, calcula_media_movel, cria_grafico_serie_historica, calcula_media_mensal

def main():
    try:
        df = busca_dados()
        df_rolling_6m = calcula_media_movel(df['Sales'], 6)
        df_rolling_12m = calcula_media_movel(df['Sales'], 12)
        cria_grafico_serie_historica(df)
        calcula_media_mensal()
        print("Gráficos gerados com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    main()