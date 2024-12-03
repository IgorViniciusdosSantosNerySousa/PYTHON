diasemana=int(input('Digite o dia da semana: 1-Segunda Feira, 2-Terça Feira...: '))

def switch(dia):
    dias= {
        1: "Segunda-Feira",
        2: "Terça-Feira",
        3: "Quarta-Feira",
        4: "Quinta-Feira",
        5: "Sexta-Feira",
        6: "Sábado",
        7: "Domingo",
    }
    
    if(dia>=8):
        print(dias.get(dia, "Dia Inválido"))
    else:
        print("O dia é: ", dias.get(dia))
        
switch(diasemana)