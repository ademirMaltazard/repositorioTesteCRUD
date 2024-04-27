import mysql.connector

def connectDB():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lojaFullStack",
    )

    cursor = conexao.cursor()
    print("Conexão como o banco de dados feita com sucesso! \n")
    return conexao, cursor


def cadastrar(nome: str, preco: float, id: str, img: str):
    ''' Faz a inserção de um produto no banco de dados. A imagem é a URL da imagem do produto na web.
    Utilizar formatos encurtados com quantidade de caracteres inferiores a 100
    Você poderá usar o https://www.encurtarlink.com/ para ajustar ao formato adequado'''

    conexao, cursor = connectDB()
    comando_sql = f"insert into produto (id_produto, nome_produto, preco_produto, image) value ('{id}', '{nome}',{preco},'{img}')"

    cursor.execute(comando_sql)
    conexao.commit()  # aqui é onde vamos inserir os dados
    print("Produto cadastrado com sucesso!")
    conexao.close()
