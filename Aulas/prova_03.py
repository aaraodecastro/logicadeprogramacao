salario = float(input("Digite o valor do seu salário: "))
meses = int(input("Digite o número de meses trabalhados: "))
x = salario / 12
ferias = x * meses
print(f"O valor das férias proporcinais é de R${ferias}")
