print("Simulador de compra com desconto")

nomeCliente = input("digite o nome do cliente: ")
nomeProduto = input("digite o nome do produto: ")
precoUnidade = float(input("digite o preço unitario do produto: "))
quantidadeProduto = float(input("digite a quantidade do produto: "))
formaPagamento = int(input("digite a forma de pagamento ( 1 pix, 2 dinheiro, 3 cartao de debito, 4 cartao de credito): "))
valorTotal = precoUnidade * quantidadeProduto
desconto = 0
juros = 0
valorFinal = valorTotal

if formaPagamento == 1:
    formaPagamentoNome = "pix"
    desconto = valorTotal * 0.10
    valorFinal = valorTotal - desconto
elif formaPagamento == 2:
    formaPagamentoNome = "dinheiro"
    desconto = valorTotal * 0.08
    valorFinal = valorTotal - desconto
elif formaPagamento == 3:
    formaPagamentoNome = "cartao de debito"
    desconto = valorTotal * 0.05
    valorFinal = valorTotal - desconto
elif formaPagamento == 4:
    formaPagamentoNome = "cartao de credito"
    print("quantas parcelas deseja fazer? (maximo 12 parcelas)")
    parcelas = int(input("digite a quantidade de parcelas: "))
    if parcelas <= 3:
        juros = 0
        valorFinal = valorTotal
    elif parcelas > 3:
        juros = valorTotal * 0.06
        valorFinal = valorTotal + juros
else:
    print("opção inválida, digite 1, 2, 3 ou 4")
    exit()

print("================================")
print("comprovante de compra")
print("================================")
print("nome do cliente:", nomeCliente)
print("nome do produto:", nomeProduto)
print("quantidade do produto: ", quantidadeProduto)
print("preço unitario do produto e quantidade do produto: ", precoUnidade, "x", quantidadeProduto, "=", valorTotal)
print("forma de pagamento:", formaPagamentoNome)

if formaPagamento in [1, 2, 3]:
    print("desconto ou juros aplicado:", desconto)
elif formaPagamento == 4:
    print("desconto ou juros aplicado:", juros)
else:
    print("desconto ou juros aplicado: 0")

print("valor final da compra:", valorFinal)