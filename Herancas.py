class ProdutoEletronico:
    def __init__(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Marca: {self.marca}, Preço: {self.preco}")

class Smartphone(ProdutoEletronico):
    def __init__(self, nome, marca, preco, armazenamento, ligado, volume):
        super().__init__(nome, marca, preco)
        self.armazenamento = armazenamento
        self.ligado = ligado
        self.volume = volume

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Armazenamento: {self.armazenamento}GB")
        if(self.ligado == True):
            print("O Celular está Ligado.")
        else:
            print("O Celular está Desligado.")
        print(f"O Volume atual é de: {self.volume}")
    
    def aumentar_volume(self):
        if(self.ligado == False):
            print("Você não pode aumentar o Volume")
        else:
            self.volume = self.volume + 10
    def diminuir_volume(self):
        if(self.ligado == False):
            print("Você não pode diminiur o Volume")
        else:
            self.volume = self.volume - 10
            
    def ligar(self):
        self.ligado = True

class Laptop(ProdutoEletronico):
    def __init__(self, nome, marca, preco, memoria_ram):
        super().__init__(nome, marca, preco)
        self.memoria_ram = memoria_ram

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Memória RAM: {self.memoria_ram}GB")

class Televisor(ProdutoEletronico):
    def __init__(self, nome, marca, preco, tamanho):
        super().__init__(nome, marca, preco)
        self.tamanho = tamanho

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tamanho: {self.tamanho}\"")

print("=========================================================")        
smar = Smartphone("IPHONE 15 PRO MAX", "APPLE", 13000, 128, True, 10)
smar.exibir_informacoes()
smar.aumentar_volume()
smar.exibir_informacoes()
smar.diminuir_volume()
smar.exibir_informacoes()

#print("=========================================================")
#smar2 = Smartphone("REDMI NOTE 12", "XIAOMI", 1000, 64, False)
#smar2.exibir_informacoes()
#print("=========================================================")
#note = Laptop("NOTEBOOK", "DELL", 7000, 32)
#note.exibir_informacoes()
#print("=========================================================")
#tv = Televisor("TV SMART", "LG", 9000, 72)
#tv.exibir_informacoes()
#print("=========================================================")
        
        
        
        
        
        
        