print ("Simulador de empréstimo")

nomeCliente = input("digite o nome do cliente:")
rendaMensal = float(input("digite a renda mensal do cliente: "))
valorEmprestimo = float(input("digite o valor do empréstimo solicitado: "))
quantidadeParcelas = int(input("digite a quantidade de parcelas desejadas: "))
valorAtrasado = float(input("digite o valor da parcela atrasada (se houver): "))

valor_parcela = valorEmprestimo / quantidadeParcelas
analise = "aprovado"

motivosNegacao = []

if valorEmprestimo > rendaMensal * 10:
    motivosNegacao.append("o valor do empréstimo solicitado é maior que 10 vezes a renda mensal do cliente.")

if valor_parcela > rendaMensal * 0.3:
    motivosNegacao.append("o valor da parcela é maior que 30% da renda mensal do cliente.")

if valorAtrasado > 0:
    motivosNegacao.append("o cliente possui parcelas atrasadas.")

if quantidadeParcelas < 1 or quantidadeParcelas > 48:
    motivosNegacao.append("a quantidade de parcelas desejadas é inválida.")

if motivosNegacao:
    analise = "negado"
    print("Empréstimo negado:")
    for motivo in motivosNegacao:
        print("-", motivo)

print ("valor do empréstimo solicitado: R$", round(valorEmprestimo, 2))
print ("quantidade de parcelas desejadas: ", quantidadeParcelas)
print ("valor da parcela: R$", round(valor_parcela, 2))
print ("resultado da analise: ", analise)