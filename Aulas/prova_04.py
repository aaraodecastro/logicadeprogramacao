salario = float(input("Digite o valor do salário: "))
dias = int(input("Digite o número de dias atrasados: "))
if dias > 5:
  tempo = dias - 5
  multa = salario * tempo * 0.02
  print("O salário está em atraso")
  print(f"O valor da multa é: R${multa}.")
else:
  print("Ainda está no prazo")
