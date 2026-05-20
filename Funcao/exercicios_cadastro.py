def cadastrar_aluno():
    aluno = {} #Dicionário
    
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["sexo"] = input("Digite o sexo do aluno: ")
    aluno["serie"] = input("Digite a série do aluno: ")
    
    aluno["disciplina"] = []
    
    qtd_disciplina = int(input("Quantas disciplinas deseja cadastrar ?"))
    
    for i in range(qtd_disciplina):
        disciplina = cadastrar_disciplinas(i)
        
        aluno["disciplina"].append(disciplina)
    
    return aluno

def cadastrar_disciplinas(i):
    disciplina = {}
    
    disciplina["nome"] = input(f"Digite o nome da {i + 1} disciplina: ")
    disciplina["notas"] = []
    
    for i in range(4):
        nota = float(input(f"Digite a {i + 1} nota: "))
        disciplina["notas"].append(nota)
    
    disciplina["media"] = calcular_media(disciplina["notas"])
    
    return disciplina

def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

def menu():
    alunos = []
    
    while True:
        print(alunos)
        print("_____ MENU ______")
        print("1 - Cadastrar Aluno")
        print("2 - Mostrar Relatório")
        print("3 - Sair")
        op = input("Escollha uma opção: ")
        
        if op == "1":
            aluno = cadastrar_aluno()
            alunos.append(aluno)
            
        elif op == "2":
            mostrar_relatorio(alunos)
            
        elif op == "3":
            print("Saindo do Sistema")
            break
        
        else:
            print("Opção inválida!!!")
            
def mostrar_relatorio(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado!!!")
    else:
        print("---- Relatório ----")
        
        for aluno in alunos:
            print("\n_________________________")
            print(f"Nome: {aluno["nome"]}")
            print(f"Idade: {aluno["idade"]}")
            print(f"Sexo: {aluno["sexo"]}")
            print(f"Serie: {aluno["serie"]}")
            
            print("\nDisciplinas:")
            
            for disciplina in aluno["disciplinas"]:
                print(f"{disciplina["nome"]} -> Média: {disciplina["media"]}:.2f")

menu()