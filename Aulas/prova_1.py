tempo_servico = float(input("Digite o tempo de serviço em anos: ")) 
valor_do_fgts = float(input("Digite o valor do FGTS: "))
if tempo_servico > 1:
    print(f"Você tem direito a multa do FGTS, o valor a receber é: {valor_do_fgts*1.4}.")
else:
    print("Não haverá multa.")
