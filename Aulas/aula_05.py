# fazer um algoritmo que roda em looping infinito
usuarios = []
while True:
    print("="*30)
    print("Cadastro de usuários")
    print("="*30)
    print("1- Cadastrar usuário")
    print("2- Atualizar Usuário")
    print("3- Deletar Usuário")
    print("4- Listar Usuário")
    print("q - Sair")
    opcao = input("Digite sua opção:")
    
    if opcao == "1":
        nome = input("Digite seu nome:")
        usuarios.append(nome)

    elif opcao == "2":
        nome=input("Digite o novo nome para atualizar:")
        elemento=int(input("Digite a posição para atualizar:"))
        usuarios[elemento]=nome

    elif opcao == "3":
        nome=input("Digite o nome para deletar:")
        usuarios.remove(nome)

    elif opcao == "4":
        for cliente in usuarios:
            print(cliente)
    elif opcao == "q":
        pass
    else:
        print("Resposta Inválida")
