import random
n = [2, 4, 7, 1, 3, 5, 6]
random.shuffle(n)
n.sort() #ordenação crescente
print(n) 
n.reverse()
print(n)

copia = list(n)
print(n)
print(copia)

n.clear()
print(n)