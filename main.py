import pandas
import streamlit as st

st.title('Sistema Dieguinho Alimentos - ME')
st.markdown('## Cadastro de produtos')

cod = st.text_input('Codigo do produto')
name = st.text_input('Nome do produto:', placeholder='Nome do produto com max de 100 caracteres')
price = float(st.number_input('Preço do produto:'))
image = st.text_input('URL da imagem do produto:', placeholder="URL com até 100 caracteres")

button = st.button('CADASTRAR')

st.write(cod)
st.write(name)
st.write(price)
st.write(image)
