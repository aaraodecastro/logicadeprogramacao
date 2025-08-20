n=int(input("Digite um número de 1 a 10"))
x=7
t=0
while n!=x:
    t=t+1
    if n>x:
        n=int(input(f"Muito alto,tente um número menor que:{n}"))
    else:
        n=int(input(f"Muito alto,tente um número maior que:{n}"))
print(f"Parabens, você acertou em {t} vezes.")

    
