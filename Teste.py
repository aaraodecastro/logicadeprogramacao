dados={
    "nome":"Zé",
    "telefone":"1",
    "e-mail":"a",
}

print("Opção 1 = Inserir nome")
print("Opção 2 = Inserir telefone")
print("Opção 3 = Inserir e-mail")
print("Opção 4 = Sair")

     


while True:

    operacao=input(print("Digite sua opção:"))
    

    if operacao == 'sair':
        print("Saindo")
        break
    elif operacao =="1":
         
         numero1 = float(input("Digite o seu nome:"))
        
         
    elif operacao =="2":

        numero2 = float(input("Digite o seu telefone:"))

    elif operacao =="3":

        numero3 = float(input("Digite o seu e-mail:"))

    else:
        print("Operação inválida. Tente novamente.")
        continue
