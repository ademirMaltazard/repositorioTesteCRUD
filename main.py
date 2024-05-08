import pandas as pd
import streamlit as st
from functionsCRUD import *

st.title('Sistema Dieguinho Alimentos - ME')

col1, col2 = st.columns(2)

containerCadastrar = col1.container(border=True)
containerAlterar = col2.container(border=True)
containerList = st.expander('Mostrar todos os produtos')

with containerCadastrar:
    containerCadastrar.markdown('## Cadastro de produtos')

    cod = containerCadastrar.text_input('Codigo do produto')
    name = containerCadastrar.text_input('Nome do produto:', placeholder='Nome do produto com max de 100 caracteres')
    price = float(containerCadastrar.number_input('Preço do produto:'))
    image = containerCadastrar.text_input('URL da imagem do produto:', placeholder="URL com até 100 caracteres")

    RegisterButton = containerCadastrar.button('CADASTRAR')

    if RegisterButton:
        RegisterNewProduct(name, price, cod, image)

with containerAlterar:
    containerAlterar.markdown('## Alterar produtos')
    newCod = containerAlterar.text_input('Novo codigo do produto')
    newName = containerAlterar.text_input('Novo nome do produto:', placeholder='Nome do produto com max de 100 caracteres')
    newPrice = float(containerAlterar.number_input('Novo preço do produto:'))
    newImage = containerAlterar.text_input('Nova URL da imagem do produto:', placeholder="URL com até 100 caracteres")

    alterButton = containerAlterar.button('Alterar')

with containerList:
    try:
        products = SearchAllproducts()
        productsTable = pd.DataFrame(products, columns=('id', 'nome', 'preço'))
        st.write(productsTable)
    except:
        containerList.write('ERROR 404. Not found.')
containerListOne = st.container(border=True)

with containerListOne:
    containerListOne.markdown("## Buscar um produto")
    id = containerListOne.text_input('ID do produto para pesquisa')
    SearchOneButton = containerListOne.button('Pesquisar')

    if SearchOneButton:
        product = SearchOneproduct(id)

        if product:
            subCol1, subCol2 = containerListOne.columns(2)
            subCol1.write(f'nome: {product[1]}')
            subCol2.write(f'Preço: {product[2]}')
            st.write('Imagem:')
            try:
                st.image(f'{product[3]}', width=200)
            except:
                st.write('Null')
            subCol3, subCol4 = containerListOne.columns(2)
            deleteButton = subCol4.button('Excluir')

            if deleteButton:
                subCol3.write("Produto excluido com sucesso!")
