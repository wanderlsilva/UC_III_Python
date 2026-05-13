nome = (input("digite o nome do paciente" ))
temperatura = float(input("digite a temperatura do paciente" ))
fda = int(input("digite 1 se o cliente estiver com falta de ar caso contrario digite qualquer outro numero" ))
if fda ==1 and temperatura >39:
    print("atendimento emergencial")
if temperatura > 37.5:
    print("o paciente",nome,"está com febre")
if fda!=1 and temperatura<37.5:
    print("paciente",nome,"está saudavel")