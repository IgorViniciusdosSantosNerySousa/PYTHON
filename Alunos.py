opcao = int(input("O que você deseja fazer? 0- Sair | 1- Realizar Média: "))
alunos = []

if(opcao > 1):
    print("Opção Inválida")
else:
    while(opcao != 0):
        if(opcao == 1):
            nomeAluno = input("Qual o Nome do Aluno?: ")
            if any(aluno['nome'] == nomeAluno for aluno in alunos): #o any verifica se ja tem algum aluno cadastrado, caso seja duplicado, ele vai dar erro.
                print(f"Erro: O Aluno '{nomeAluno}' já está cadastrado. Use outro nome.")
            else:
                n1 = float(input("Digite a 1º nota: "))
                n2 = float(input("Digite a 2º nota: "))
                n3 = float(input("Digite a 3º nota: "))
                n4 = float(input("Digite a 4º nota: "))

                media = (n1 + n2 + n3 + n4)
                print(f'A Média do(a) {nomeAluno} é de: {media}')
                
                alunos.append({'nome': nomeAluno, 'media': media})
        
        opcao = int(input("O que você deseja fazer? 0- Sair | 1- Realizar Média: "))
    
    print("\nAlunos cadastrados:") #\n ele pula uma linha pra baixo
    for aluno in alunos:
        print(f"Aluno: {aluno['nome']}, Média: {aluno['media']:.1f}")
    
    else:
        print("Programa Finalizado.")