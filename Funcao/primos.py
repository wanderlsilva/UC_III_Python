def testar_primo(n):
    teste = 1
    for i in range(2, n):
        if n % i == 0:
            teste = teste + 1
    if teste != 1:
        print("Não é Primo")
    else:
        print("É primo")

testar_primo(6)