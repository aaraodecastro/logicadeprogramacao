nunerousuario=int(input("Digite um número de 1 a 10"))
numerocerto=7
t=0
while nunerousuario!=numerocerto:
    t=t+1
    if nunerousuario>numerocerto:
        nunerousuario=int(input(f"Muito alto,tente um número menor que:{n}"))
    else:
        nunerousuario=int(input(f"Muito alto,tente um número maior que:{n}"))
print(f"Parabens, você acertou em {t} vezes.")

    
