febre=input("Você está com febre?: Sim - Não: ")
tosse=input("Você está com tosse?: Sim - Não: ")

febre = febre.upper()
tosse = tosse.upper()

if(febre=="SIM"):
    print("Gripe")
elif(tosse=="SIM"):
    print("Infecção")
else:
    print("Consulte um Médico, as vezes é bom mesmo não estando doente!")