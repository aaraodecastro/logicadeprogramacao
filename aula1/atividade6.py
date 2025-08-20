# comentario de uma linha 
'''
Crie um programa que leia números inteiros e 
substiua  maior pela diferença e escreva ambos no console
'''

primeiro_numero=input("Digite um número inteiro: ")
primeiro_numero=int(primeiro_numero)

segundo_numero=int(input("Digite um número inteiro: "))

pr=primeiro_numero-segundo_numero
while pr!=0:
    if primeiro_numero>segundo_numero:
        primeiro_numero=primeiro_numero-segundo_numero
    else: segundo_numero=segundo_numero-primeiro_numero
    pr=primeiro_numero-segundo_numero

print(primeiro_numero)
