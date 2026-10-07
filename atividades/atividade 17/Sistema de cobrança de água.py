print("Sistema de Cobrança de Água")

nomeCliente = input("digite o nome do cliente: ")
consumoAgua = float(input("digite o consumo de água em metros cúbicos: "))

tipoInstalacao = input("digite o tipo de instalação (R Residencial, C Comercial ou 1/2): ").upper()

if consumoAgua < 0:
    print("consumo inválido. O consumo não pode ser negativo.")
    exit()

if tipoInstalacao in ("R", "1"):
    tipoInstalacaoNome = "Residencial"
    if consumoAgua <= 10:
        tarifa = 2.00
    elif consumoAgua <= 20:
        tarifa = 3.00
    else:
        tarifa = 4.50
elif tipoInstalacao in ("C", "2"):
    tipoInstalacaoNome = "Comercial"
    if consumoAgua <= 10:
        tarifa = 3.50
    elif consumoAgua <= 20:
        tarifa = 5.00
    else:
        tarifa = 7.00
else:
    print("opção inválida, digite R, C, 1 ou 2")
    exit()

valorConta = consumoAgua * tarifa
taxaFixa = 12.00

if consumoAgua > 30:
    multa = valorConta * 0.10
else:
    multa = 0.00

if consumoAgua <= 10:
    classificacao = "baixo"
elif consumoAgua <= 20:
    classificacao = "moderado"
else:
    classificacao = "elevado"

valorTotal = valorConta + taxaFixa + multa

print("nome do consumidor: ", nomeCliente)
print("consumo registrado: ", consumoAgua, "m3")
print("tipo de imóvel: ", tipoInstalacaoNome)
print("tarifa utilizada: R$", round(tarifa, 2), "por m3")
print("taxa de serviço: R$", round(taxaFixa, 2))
print("multa: R$", round(multa, 2))
print("valor total da conta: R$", round(valorTotal, 2))
print("classificação do consumo: ", classificacao)
