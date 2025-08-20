import random

try:
    
    numerocerto = random.randint(1,10)
    numerousuario=int(input("Digite um número de 1 a 10"))
    t=1
    while numerousuario!=numerocerto:
        t=t+1
        if numerousuario>numerocerto:
            numerousuario=int(input(f"Muito alto,tente um número menor que{numerousuario}:"))
        else:
            numerousuario=int(input(f"Muito baixo,tente um número maior que:{numerousuario}:"))
    print(f"Parabens, você acertou em {t} vezes.")
except:
    print("Entrada não válida")
    
