import yfinance as yf 
import streamlit as st 
from PIL import Image
from urllib.request import urlopen
import requests

##_________________________________________________________
st.set_page_config(layout="wide")

st.sidebar.image('BITCOIN/binance-logo-0.png', use_column_width=True)
st.header(":orange[Bitcoin Dashboard]", divider='rainbow')
st.subheader(':blue[Lista de preço Altos e Baixos]')


BASE_URL = 'https://api.github.com'
def selecionarUsuario(username):
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Pesquise sobre a sua cripto para descobrir o GITHUB ')
    username = st.text_input('_Insira o a sua Cripto_')
  
    if st.button('Buscar'):
         infoUsuario = selecionarUsuario(username)
         if infoUsuario is not None:
              st.markdown(f'''<div class="card" style="width: 18rem;">
  <img src="{infoUsuario['avatar_url']}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">{infoUsuario['login']}</h5>
    <p class="card-text">{infoUsuario['bio']}</p>
    <a href="{infoUsuario['html_url']}" sytle="color: white; text-decoration: none;" class="btn btn-primary">Ver Perfil</a>
  </div>
</div>

              ''',unsafe_allow_html=True)

ui()




