import mysql.connector

def ConnectDB():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lojaFullStack",
    )

    cursor = conexao.cursor()
    print("Conexão como o banco de dados feita com sucesso! \n")
    return conexao, cursor


def RegisterNewProduct(nome: str, preco: float, id: str, img: str):
    '''Faz a inserção de um produto no banco de dados. A imagem é a URL da imagem do produto na web.
    Utilizar formatos encurtados com quantidade de caracteres inferiores a 100
    Você poderá usar o https://www.encurtarlink.com/ para ajustar ao formato adequado'''

    conexao, cursor = ConnectDB()
    query = (f"insert into produto (id_produto, nome_produto, preco_produto, image) "
             f"value ('{id}', '{nome}',{preco},'{img}')")

    cursor.execute(query)
    conexao.commit()  # aqui é onde vamos inserir os dados
    print("Produto cadastrado com sucesso!")
    conexao.close()
    
def DeleteProductByID(id):
    conexao, cursor = ConnectDB()
    query = f"DELETE FROM produto WHERE (id_produto='{id}')"
    cursor.execute(query)
    conexao.commit()
    conexao.close()
    return print('Produto deletado com sucesso!')

def SearchAllproducts():
    conexao, cursor = ConnectDB()
    query = f'SELECT id_produto, nome_produto, preco_produto FROM produto'
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def SearchOneproduct(id):
    conexao, cursor = ConnectDB()
    query = f'SELECT * FROM produto WHERE id_produto = "{id}"'
    cursor.execute(query)
    result = cursor.fetchone()
    return result
