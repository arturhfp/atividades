print ("Sistema de Abastecimento e Viagem")

distanciaViagem = float(input("digite a distância da viagem em km: "))
consumoCombustivel = float(input("digite o consumo de combustível do veículo em km/litro: "))
quantidadeDisponivel = float(input("digite a quantidade de combustível disponível no veículo em litros: "))
precoCombustivel = float(input("digite o preço do combustível por litro: "))
pedagios = input("possui pedágios na viagem? (s/n): ")
litros_necessarios = distanciaViagem / consumoCombustivel
custo_combustivel = litros_necessarios * precoCombustivel
if pedagios.lower() == "s":
    quantidadePedagios = int(input("digite a quantidade de pedágios na viagem: "))
    valorPedagio = float(input("digite o valor do pedágio: "))
    custo_pedagios = quantidadePedagios * valorPedagio
    custo_total = custo_combustivel + custo_pedagios
else:
    custo_pedagios = 0.0    
    custo_total = custo_combustivel + custo_pedagios

print ("litros de combustível necessários: ", round(litros_necessarios, 2))
print ("custo do combustível: R$", round(custo_combustivel, 2))
print ("custo dos pedágios: R$", round(custo_pedagios, 2))
print ("custo total da viagem: R$", round(custo_total, 2))
print ("tem combustível suficiente para a viagem? ", "Sim" if quantidadeDisponivel >= litros_necessarios else "Não")
print("quantos litros de combustível faltam para a viagem: ",
      round(litros_necessarios - quantidadeDisponivel, 2) if quantidadeDisponivel < litros_necessarios else 0.0)


