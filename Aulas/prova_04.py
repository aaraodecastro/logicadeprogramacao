num1 = int(input("Digite o primério número do seu intervalo: "))
num2 = int(input("Digite o segundo número do seu intervalo: "))
par = False
soma = 0
for numero in range(num1,num2 + 1):
  if numero %2 == 0:
    soma = soma + numero
    par = True
else:
  if not par:
    print("Não existe pares nesse intervalo")
print(f"A soma dos números pares desse intervalo é {soma}")
