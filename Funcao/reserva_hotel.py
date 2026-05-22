reservas = []

tipos_quartos = ("Standard", "Luxo", "Premium")

def menu():
    while True:
        print("\n ====== SISTEMA DE RESERVA DE HOTEL ====== ")
        print("1 - Cadastrar reserva")
        print("2 - Relatório ")
        print("3 - Sair")
        
        opcao = int(input("Escolha um opção: "))
        
        if opcao == 1:
            cadastrar_reserva()
        elif opcao == 2:
            mostrar_relatorio()
        elif opcao == 3:
            print("Sistema encerrado.")
            break
        else:
            print("\n Opção inválida!!!. Tente novamente")

def cadastrar_reserva():
    try:
        hospede = {}
        
        hospede['nome'] = input("Digite o nome do hóspede: ")
        
        if hospede['nome'] == "":
            print("Erro!!! O campo nome não pode estar vazio")
            return
        
        hospede['idade'] = int(input("Digite a idade: "))
        
        if hospede['idade'] <= 0:
            print("Erro!!! A idade deve ser maior que ZERO.")
            return
        
        hospede['cpf'] = int(input("Digite os numeros do CPF: "))
        
        if len(str(hospede['cpf'])) < 10 or len(str(hospede['cpf'])) > 11:
            print("Erro!!! Numero de CPF inválido.")
            return
        
        print("\n Tipos de quartos disponiveis: ")
        for tipo in tipos_quartos:
            print(f" - {tipo}")
            
        hospede['tipo_quarto'] = input("Digite o tipo do Quarto: ")
        
        if hospede['tipo_quarto'] not in tipos_quartos:
            print("Erro!!! Tipo de quarto inválido.")
            return
        
        hospede['diarias'] = int(input("Digite a quantidade de diárias: "))
        
        if hospede["diarias"] <= 0:
            print("Erro!!! A quantidade de diarias deve ser maior que zero.")
            return
        
        hospede['valor_total'] = calcular_valor_total(hospede['tipo_quarto'], hospede["diarias"])
        
        hospede['situacao'] = classificar_reserva(hospede["valor_total"])
        
        reservas.append(hospede)
        
        print("\n Reserva cadastrada com Sucesso!!!")
        
    except (ValueError, TypeError):
        print("\n Erro!!! Digite numeros válidos para idade, diárias e CPF")
        
    finally:
        print("Operação Concluida com Sucesso.")
        
        
def calcular_valor_total(tipo_quarto, diarias):
    if tipo_quarto == "Standard":
        return 120 * diarias
    elif tipo_quarto == "Luxo":
        return 250 * diarias
    else:
        return 400 * diarias

def classificar_reserva(valor_total):
    if valor_total <= 500:
        return "Reserva Econômica"
    elif valor_total <= 1500:
        return "Reserva Intermediária"
    else:
        return "Reserva Premium"
    
def mostrar_relatorio():
    if len(reservas) == 0:
        print("\n Nenhuma reserva cadastrada.")
    else:
        print("\n **** RELATÓRIO DE RESERVAS ****")
        
        for hospede in reservas:
            print("-------------------")
            print(f"Nome: {hospede['nome']}")
            print(f"Idade: {hospede['idade']}")
            print(f"Cpf: {hospede['cpf']}")
            print(f"Tipo de Quarto: {hospede['tipo_quarto']}")
            print(f"Diárias: {hospede['diaria']}")
            print(f"Valor Total: {hospede['valor_total']}")
            print(f"Situação: {hospede['situacao']}")
            
menu()