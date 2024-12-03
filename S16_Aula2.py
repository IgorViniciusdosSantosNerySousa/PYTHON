risco=str(input("Qual é o seu tipo de Risco: Operacional/Financeiro/Mercado"))

risco=risco.upper()

if(risco=="OPERACIONAL"):
    print("O seu Risco é Operacional, Verifique seu sistema.")
elif(risco=="FINANCEIRO"):
    print("O seu Risco é Financeiro. Procure um Trabalho urgente.")
else:
    print("O seu Risco é de Mercado. Traga melhorias a ele.")