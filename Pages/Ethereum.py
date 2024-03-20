import yfinance as yf 
import streamlit as st 
from PIL import Image
from urllib.request import urlopen


##
st.sidebar.image('BITCOIN/binance-logo-0.png', use_column_width=True)
st.title("Preços Diários de Criptomoedas")
st.header(":orange[Bitcoin Dashboard]", divider='rainbow')
st.subheader(':blue[Lista de preço Altos e Baixos]')

##
Ethereum = "ETH-USD"
##
ETH_DATA = yf.Ticker(Ethereum)
##
ETHHis = ETH_DATA.history(period="max")
##
ETH = yf.download(Ethereum, start="2021-11-17", end="2021-11-18")

## Titulo
st.write(":blue[_ETHEREUM_ ($)]")
## Carregamento da Logo do Bitcoin
imageETH = Image.open('BITCOIN/ethereum logo.png')
st.image(imageETH)
## Tabela de Dados de Bitcoin
st.table(ETH)
##  Gráfico de Linha com os dados
st.bar_chart(ETHHis.Close)
