par=0
impar=0
positivo=0
negativo=0
neutro=0

for num in range(5):
    num=int(input("Digite um número: "))
    if (num % 2 == 0):
        par+=1
    else:
        impar+=1
        
    if(num<0):
        negativo+=1
    elif(num>0):
        positivo+=1
    elif(num==0):
        neutro+=1
  
print(f"Quantidade de Números Pares: {par}")
print(f"Quantidade de Números Impares: {impar}")
print(f"Quantidade de Números Positivos: {positivo}")
print(f"Quantidade de Números Negativos: {negativo}")
print(f"Quantidade de Números Neutros: {neutro}")
