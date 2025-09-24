
clientes = []
from time import sleep
import os 
from random import choice

while True:
    print("="*30)
    print("Doceria do Zé".center(30))
    print("="*30)
    cliente = {}
    cliente["nome"] = input("Digite seu nome:")
    if cliente["nome"] == "sair":
        break
    cliente["telefone"] = input("Digite seu telefone:")
    cliente["email"] = input("Digite seu email:")
    clientes.append(cliente)
    print("\033[31mCliente Adicionado Com sucesso!  \033[m")
    sleep(5)
    os.system("clear")
    
print(clientes)

cliente_sorteado = choice(clientes)
print(f"Parabéns {cliente_sorteado["nome"]} Você foi sorteado!")

=========================================================
