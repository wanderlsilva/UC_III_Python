produtos = []
def cadastrar_produto():
    try:
        produto = {}
        produto['nome'] = input("Digite um nome: ")
        produto['quantidade'] = int(input("Digite a qauntidade: "))
        produto['preco'] = float(input("Digite o preço: "))
        produtos.append(produto)
        print("Produto cadastrado com sucesso !!!")
    
    except ValueError:
        print("Erro! Quantidade e preço devem ser numericos. ")
    
    finally:
        print("Produto finalizado. ")
        
cadastrar_produto()