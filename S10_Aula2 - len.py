senha=input('Digite uma senha que contenha pelo menos 8 caractéres, incluindo letras e números: ')

senha1=len(senha)
print(senha1)

if(any(char.isdigit() for char in senha)==True):
    print('Contém números.')
if(any(char.isalpha() for char in senha)==True):
    print('Contém letras')
  
tamanho = len(senha) 
if(tamanho>8):
    print('Digite uma senha até 8 caracteres. Tente novamente.')
