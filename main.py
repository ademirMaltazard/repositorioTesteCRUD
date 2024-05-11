import pandas as pd
import streamlit as st
from functionsCRUD import *

st.title('Sistema Dieguinho Alimentos - ME')
pagina1, pagina2, pagina3, pagina4 = st.tabs(["Listar Produtos", "Cadastrar", "Atualizar", "Buscar Produto"])

with pagina1:
    try:
        products = SearchAllProducts()
        productsTable = pd.DataFrame(products, columns=('id', 'nome', 'preço'))
        if productsTable.__len__() == 0:
            pagina1.write("## Nenhum produto cadastrado!")
        else:
            pagina1.write(productsTable)

    except:
        pagina1.write('ERROR 404. Not found.')
    pagina1.button("atualizar pagina")


with pagina2:
    pagina2.markdown('## Cadastro de produtos')

    cod = pagina2.text_input('Codigo do produto')
    name = pagina2.text_input('Nome do produto:', placeholder='Nome do produto com max de 100 caracteres')
    price = float(pagina2.number_input('Preço do produto:'))
    image = pagina2.text_input('URL da imagem do produto:', placeholder="URL com até 100 caracteres")

    RegisterButton = pagina2.button('CADASTRAR')

    if RegisterButton:
        RegisterNewProduct(name, price, cod, image)

productForUpdate = None
with pagina3:
    pagina3.markdown('## Alterar produtos')
    id = pagina3.text_input('Novo codigo do produto')
    SearchOneButton = pagina3.button('Buscar para alterar')

    if SearchOneButton:
        productForUpdate = SearchOneProduct(id)
        if productForUpdate != None:
            newName = pagina3.text_input('Novo nome do produto:', value=productForUpdate[1], placeholder='Nome do produto com max de 100 caracteres')
            newPrice = float(pagina3.number_input('Novo preço do produto:', value=productForUpdate[2]))
            newImage = pagina3.text_input('Nova URL da imagem do produto:', value=productForUpdate[3], placeholder="URL com até 100 caracteres")

    def Update():
        result = UpdateProduct(id, newName, newPrice, newImage)
        print('result: ', result)

    if productForUpdate != None:
        alterButton = pagina3.button('Alterar', on_click=Update)

productForDelete = None
with pagina4:
    pagina4.markdown("## Buscar um produto")
    id = pagina4.text_input('ID do produto para pesquisa')
    SearchOneButton = pagina4.button('Pesquisar')

    if SearchOneButton:
        productForDelete = SearchOneProduct(id)

        if productForDelete:
            subCol1, subCol2 = pagina4.columns(2)
            subCol1.write(f'nome: {productForDelete[1]}')
            subCol2.write(f'Preço: {productForDelete[2]}')
            pagina4.write('Imagem:')
            try:
                pagina4.image(f'{productForDelete[3]}', width=200)
            except:
                pagina4.write('Null')

    def delete():
        result = DeleteProductByID(id)
        if result == None:
            result = "Produto não encontrado!!!"
        pagina4.write(result)

    if productForDelete != None:
        deleteButton = pagina4.button('Excluir produto', on_click=delete)
        print(deleteButton)
