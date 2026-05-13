distancia = int (input ("qual a distancia da sua entrega?"))
print ("seu produto é urgente?")
produto = int (input("responda: 1- Sim, 2- Não"))

if produto == 1:
    print ("Seu produto é urgente")
    if distancia >=300:
        print ("entrega longa")
elif distancia <300:
    print ("entrega comum")
 
        
    
