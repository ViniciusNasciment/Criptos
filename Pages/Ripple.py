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

Ripple = "XRP-USD"

##

XRP_DATA = yf.Ticker(Ripple)

##

XRPHis = XRP_DATA.history(period="max")
##


XRP = yf.download(Ripple, start="2021-11-17", end="2021-11-18")


## Titulo
st.write(":blue[BITCOIN ($)]")
## Carregamento da Logo do Bitcoin
imageXRP = Image.open('BITCOIN/Ripple.png')
st.image(imageXRP)
## Tabela de Dados de Bitcoin
st.table(XRP)
##  Gráfico de Linha com os dados
st.bar_chart(XRPHis.Close)
