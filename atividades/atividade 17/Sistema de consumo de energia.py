print ("Sistema de consumo de energia")

nomeConsumidor = input("digite o nome do consumidor:")
consumoMensal = float(input("digite o consumo mensal em kWh: "))
tipoInstalacao = input("digite o tipo de instalação (R Residencial, C Comercial, I Industrial): ")
if tipoInstalacao == "R":
    tipoInstalacaoNome = "Residencial"
    if consumoMensal <= 100:
        valorConta = consumoMensal * 0.60
    elif consumoMensal >= 101:
        valorConta = consumoMensal * 0.75
elif tipoInstalacao == "C":
    tipoInstalacaoNome = "Comercial"
    if consumoMensal <= 100:
        valorConta = consumoMensal * 0.70
    elif consumoMensal >= 101:
        valorConta = consumoMensal * 0.85
elif tipoInstalacao == "I":
    tipoInstalacaoNome = "Industrial"
    if consumoMensal <= 100:
        valorConta = consumoMensal * 0.80
    elif consumoMensal >= 101:
        valorConta = consumoMensal * 0.95
else:
    print("opção inválida, digite R, C ou I")
    exit()
taxaFixa = 15.00
impostoConsumo = valorConta * 0.12

if consumoMensal <= 100:
    print ("o consumo esta em baixo nivel, parabens!")
elif consumoMensal <= 250:
    print ("o consumo esta em uso moderado, cuidado!")
elif consumoMensal <= 500:
    print ("o consumo esta em  nivel elevado, atenção!")
else:
    print ("o consumo esta em nivel muito elevado, cuidado!")

print ("nome do consumidor: ", nomeConsumidor)
print ("tipo de instalação: ", tipoInstalacaoNome)
print ("consumo mensal: ", consumoMensal, "kWh")
print ("valor da conta: R$", round(valorConta, 2))
print ("taxa fixa: R$", round(taxaFixa, 2))
print ("imposto sobre o consumo: R$", round(impostoConsumo, 2))
print ("valor total da conta: R$", round(valorConta + taxaFixa + impostoConsumo, 2))
print ("classificação do consumo: ", end="")
if consumoMensal <= 100:
    print ("baixo")
elif consumoMensal <= 250:
    print ("moderado")
elif consumoMensal <= 500:
    print ("elevado")
else:
    print ("muito elevado")
print ("obrigado por utilizar o sistema de consumo de energia!")
