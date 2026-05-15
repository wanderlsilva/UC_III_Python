'''CRIE UM PROGRAMA NO QUAL O USUÁRIO INFORME 2 NUMEROS INTEIROS: A e B.
PARA QUE O PROGRAMA CONTINUE SUA EXECUÇÃO, VERIFIQUE SE A < B. 
SE SIM, CALCULE A SOMA DOS NUMEROS INTEIROS NO INTERVALO [A,B].
CASO CONTRÁRIO, INFORME UMA MENSAGEM DE ERRO.'''

a = int(input("Informe um numero: "))
b = int(input("Informe outro numero: "))

if a < b:
    soma = 0
    for x in range(a, b + 1):
        soma = soma + x
    print(f"Soma dos inteiros no intervalo de {a} e {b} é: {soma}")
else:
    print("Erro. A deve ser menor que B.")