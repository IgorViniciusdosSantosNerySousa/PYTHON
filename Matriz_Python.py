Quartos = [["Ocupado", "Ocupado", "Vazio"],
           ["Ocupado", "Vazio", "Vazio"], 
           ["Vazio", "Vazio", "Vazio"]]
vazios=0
print("|====================================================================================================================|")
print("|Quartos Disponíveis:", Quartos)
for linha in Quartos:
    for vazio in linha:
        if(vazio=="Vazio"):
            vazios=vazios+1
            
print("|====================================================================================================================|")
print("|Quantidade de Quartos Vazios: ", vazios)
print("|====================================================================================================================|")
            

            
        