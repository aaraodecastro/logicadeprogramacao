hora_trabalhada = int(input("Digite a quantidades de horas trabalhadas: "))
valor_hora = float(input("Digite o valo da hora normal: "))
if hora_trabalhada == 44:
  print("Você cumpriu sua horas semanais corretamente.")
elif hora_trabalhada > 44:
  restante = hora_trabalhada - 44
  bonus = restante * valor_hora * 1.5
  print(f"Você possui {restante} hora(s) além do determinado, você deve receber R${bonus}.")
else:
  print(f"Você ainda deve {44 - hora_trabalhada} hora(s).")
