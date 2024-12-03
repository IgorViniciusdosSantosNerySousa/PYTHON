opcao = int(input("O que você deseja fazer? 0- Sair | 1- Comprar Peças: "))
if(opcao > 1):
    print("Opção Inválida")
else:
    while(opcao != 0):
        if(opcao == 1):
            qtdPecas = int(input("Quantas Peças você irá comprar?: "))
            preco = float(input("Digite o Preço p/Peça: "))

            def semDesconto():
                precoTotal = preco * qtdPecas
                print(f'Preço Total: {precoTotal:,.2f}')
    
            def com10Desconto():
                desconto10 = preco * 0.1 
                precoTotal1 = (preco - desconto10) * qtdPecas
                print(f"Preço Total: {precoTotal1:,.2f}")
    
            def com20Desconto():
                desconto20 = preco * 0.2
                precoTotal2 = (preco - desconto20) * qtdPecas
                print(f"Preço Total: {precoTotal2:,.2f}")
    
            if(qtdPecas <= 5):
                print("Sem Desconto Adicional.")
                semDesconto()
            elif(qtdPecas >= 6 and qtdPecas<=10):
                print("Você Obteve 10% de Desconto!")
                com10Desconto()
            elif(qtdPecas > 10):
                print("Você Obteve 20% de Desconto!")
                com20Desconto()
        opcao = int(input("O que você deseja fazer? 0- Sair | 1- Comprar Peças: "))
    else:
        print("Programa Finalizado.")