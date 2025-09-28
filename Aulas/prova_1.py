tempo_servico = int(input("Digite o tempo de serviço em anos: ")) 
valor_do_fgts = 10000
if tempo_servico > 1:
    print(f"Você tem direito a multa do FGTS, o valor a receber é: {valor_do_fgts*0.4}.")
else:
    print("Não haverá multa.")
