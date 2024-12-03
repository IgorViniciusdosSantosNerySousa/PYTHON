opcao = int(input("O que deseja Fazer? 0- Sair | 1- Adicionar um Item | 2- Remover um Item | 3- Exibir Minha Lista: "))
lista_compras = []

if(opcao > 3):
    print("Opção Inválida")
else:
    while(opcao != 0):
        if(opcao == 1):
            item = input("Item Desejado: ")
            lista_compras.append(item)
            print(f"'{item}' foi adicionado à lista.")

        elif(opcao == 2):
            item = input("Digite o nome do Item você irá remover: ")
            if(item in lista_compras):
                lista_compras.remove(item)
                print(f"'{item}' foi removido da lista.")
            else:
                print(f"'{item}' não está na lista de compras.")

        elif(opcao == 3):
            if(lista_compras):
                print("\nLista de Compras:")
                for i, item in enumerate(lista_compras, start=1):
                    print(f"{i}. {item}")
            else:
                print("A lista de compras está vazia.")
        opcao = int(input("O que deseja Fazer? 0- Sair | 1- Adicionar um Item | 2- Remover um Item | 3- Exibir Minha Lista: "))
        
    else:
        print("Programa Finalizado.")

