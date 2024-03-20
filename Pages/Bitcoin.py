import yfinance as yf 
import streamlit as st 
from PIL import Image
from urllib.request import urlopen


##_________________________________________________________
st.set_page_config(layout="wide")
##
st.sidebar.image('BITCOIN/binance-logo-0.png', use_column_width=True)
st.title("Preços Diários de Criptomoedas")
st.header(":orange[Bitcoin Dashboard]", divider='rainbow')
st.subheader(':blue[Lista de preço Altos e Baixos]')
##
Bitcoin = "BTC-USD"
##
BTC_DATA = yf.Ticker(Bitcoin)
##
BTCHis = BTC_DATA.history(period="max")
#
BTC = yf.download(Bitcoin, start="2021-11-17", end="2021-11-18")
## Titulo
st.write(":blue[BITCOIN ($)]")
## Carregamento da Logo do Bitcoin
imageBTC = Image.open('BITCOIN/BIT_COINS_BRANCO-removebg-preview.png')
st.image(imageBTC)
## Tabela de Dados de Bitcoin
st.table(BTC)
##  Gráfico de Linha com os dados
st.bar_chart(BTCHis.Close)



