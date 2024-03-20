import yfinance as yf 
import streamlit as st 
from PIL import Image
from urllib.request import urlopen
import time


st.set_page_config(layout="wide")

##
st.sidebar.image('BITCOIN/binance-logo-0.png', use_column_width=True)
st.title("Preços Diários de Criptomoedas")
st.header(":green[Bitcoin Dashboard]", divider='rainbow')
st.subheader(':green[Lista de preço Altos e Baixos]')

##

BitcoinCash = "BCH-USD"

##

BCH_DATA = yf.Ticker(BitcoinCash)

##

BCHHis = BCH_DATA.history(period="max")

##

BCH = yf.download(BitcoinCash, start="2021-11-17", end="2021-11-18")

## Titulo
st.write(":green[BITCOIN CASH ($)]")
## Carregamento da Logo do Bitcoin
imageBCH = Image.open('BITCOIN/BitcoinCash.png')
st.image(imageBCH)
## Tabela de Dados de Bitcoin
st.table(BCH)
##  Gráfico de Linha com os dados
st.bar_chart(BCHHis.Close)



