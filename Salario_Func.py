print("|=======================================================|")
num_func = int(input("|Digite o número do funcionário: "))
print("|=======================================================|")
h_trab = int(input("|Digite o número de horas trabalhadas: "))
print("|=======================================================|")
vph = float(input("|Digite o valor que o funcionário recebe por hora: "))
print("|=======================================================|")

salario = h_trab * vph

print("|Calculando o Salário...")
print("|=======================================================|")
print(f"|Número do Funcionário: {num_func}|")
print("|=======================================================|")
print(f"|O Salário do Funcionário é de: ${salario:.2f} Dólares|")
print("|=======================================================|")
