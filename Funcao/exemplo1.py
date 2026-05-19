dados = [] #Lista Vazia
disciplinas = []
def cadastrar_aluno():
    nome = input("Informe o nome do aluno: ")
    idade = int(input("Informe a idade: "))
    sexo = input("Informe o sexo: F - Feminino / M - Masculino ")
    dados.append([nome, idade, sexo])
    print("Aluno Cadastro com Sucesso!!!")

def cadastrar_disciplinas():
    disciplina = input("Informe nome da Disciplina: ")
    ch = int(input("Informe a Carga Horária: "))
    disciplinas.append([disciplina, ch])
    print("Disciplinas Cadastradas!!")

while True:
    print("---Sistema Academico---")
    print(" 1 - Cadastrar Aluno ")
    print(" 2 - Cadastrar Disciplina ")
    op = int(input("Informe o que deseja: "))
    
    if op == 1:
        cadastrar_aluno()
    elif op == 2:
        cadastrar_disciplinas()
    else:
        print("Saindo do Sistema...")