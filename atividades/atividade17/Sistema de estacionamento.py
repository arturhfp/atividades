print ("Sistema de estacionamento")

placaCarro = input("digite a placa do carro: ")
quantidadeHoras = float(input("digite a quantidade de horas que o carro ficou estacionado: "))
valor =  0.00
desconto = 0.00
valorFinal = 0.00

if quantidadeHoras <=1: 
    valor =  8.00   
elif quantidadeHoras > 1   and quantidadeHoras <= 3:
    valor =  15.00
elif quantidadeHoras > 3 and quantidadeHoras <= 6:
    valor =  25.00
else:
    valor =  40.00

clienteCadastrado = input("o cliente possui cadastro? (sim/não): ")
if clienteCadastrado == "sim":
        desconto = valor * 0.10
        valorFinal = valor - desconto
        print("o cliente possui cadastro, desconto de 10% aplicado")
elif clienteCadastrado == "não":
    valorFinal = valor
    print("o cliente não possui cadastro, sem desconto aplicado")
else:
    print("opção inválida, digite sim ou não")
print(f"placa do carro: {placaCarro}")
print(f"quantidade de horas: {quantidadeHoras}")
print(f"valor  a pagar: {valor}")
print(f"desconto aplicado: {desconto}")
print(f"valor final a pagar: {valorFinal}")
        