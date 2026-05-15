import random
nomes = []

while True:
    nome = input("Digite um nome: ")
    nomes.append(nome)
    
    op = input("Deseja continuar [S][N]?")
    if op.upper() == "N":
        break
print(nomes)

random.shuffle(nomes) #Shuffle embaralhar dados
#print(f"Lista embaralhada: {nomes}")
sorteio = random.choice(nomes) #Choice sortear um dado
print(f"O nome do sortudo é: {sorteio}")

while True:
    sorteio_2 = int(input("Deseja realizar outro sorteio? 1 - SIM OU 0 - NAO"))
    if sorteio_2 == 1:
        nomes.remove(sorteio)
        print(nomes)
        sorteio = random.choice(nomes)
        print(f"O nome do sortudo é: {sorteio}")
    else:
        print("Fim do sorteio.")
        break