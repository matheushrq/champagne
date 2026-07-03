from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# print(plt.style.available) -- tipos de gráfico para estilizar

def busca_dados():
    link = ('https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly_champagne_sales.csv')
    df = pd.read_csv(link, index_col=0, parse_dates=True)
    return df

df = busca_dados()
GRAFICOS_DIR = Path(__file__).resolve().parent / 'graficos'

# Médias móveis
def calcula_media_movel(df, window):
    return df.rolling(window=window).mean()

# Série histórica
def cria_grafico_serie_historica(df):

    GRAFICOS_DIR.mkdir(exist_ok=True)

    plt.style.use('seaborn-v0_8-dark')
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle('Série Histórica de Vendas de Champanhe', fontsize=20, fontweight='bold')
    ax.plot(df['Sales'], color='blue', label='Vendas de Champanhe')

    ax.set_xlabel('Meses/Anos', fontsize=14, labelpad=20)
    ax.set_ylabel('Unidades vendidas no mês', fontsize=14, labelpad=20)

    ax.legend(fontsize=12, loc='upper center', ncol=3)
    fig.savefig(GRAFICOS_DIR / 'serie_historica_vendas_champanhe.png', dpi=300, bbox_inches='tight')
    plt.show()
    plt.close(fig)

def calcula_media_mensal():
    GRAFICOS_DIR.mkdir(exist_ok=True)
    df_monthly_means = df.groupby(df.index.month).mean()
    ax = df_monthly_means.plot(
        kind='bar',
        figsize=(12, 6),
        color='orange',
        title='Média Mensal de Vendas de Champanhe',
        xlabel='Mês',
        ylabel='Unidades vendidas no mês'
    )
    ax.figure.savefig(GRAFICOS_DIR / 'media_mensal_vendas_champanhe.png', dpi=300, bbox_inches='tight')
    plt.close(ax.figure)