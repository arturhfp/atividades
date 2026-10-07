print ("Sistema de ingresso para evento")

nomeParticipante = input("digite o nome do participante:")
idadeParticipante = int(input("digite a idade do participante: "))
tipoIngresso = input("digite o tipo de ingresso (A Aluno, P Professor, PG Publico Geral): ").upper()
if tipoIngresso == "A":
    tipoIngressoNome = "Aluno"
    valorIngresso = 20.00
elif tipoIngresso == "P":
    tipoIngressoNome = "Professor"
    valorIngresso = 25.00
elif tipoIngresso == "PG":
    tipoIngressoNome = "Publico Geral"
    valorIngresso = 40.00
else:
    print("opção inválida, digite A, P ou PG")
    exit()

quantidadeIngressos = int(input("digite a quantidade de ingressos: "))
valorTotal = valorIngresso * quantidadeIngressos

descontoIdade = 0.0
descontoQuantidade = 0.0

if idadeParticipante < 10:
    print ("o participante é uma criança, entrada gratuita!")
    descontoIdade = valorTotal
elif idadeParticipante >= 60:
    print ("o participante é um idoso, desconto de 50%!")
    descontoIdade = valorTotal * 0.5
else:
    print ("o participante é um adulto, sem desconto!")

if quantidadeIngressos > 5:
    print ("quantidade de ingressos acima de 5, desconto de 10%!")
    descontoQuantidade = valorTotal * 0.10
else:
    print ("quantidade de ingressos dentro do limite, sem desconto!")

valorDesconto = max(descontoIdade, descontoQuantidade)
valorTotal = valorTotal - valorDesconto

print ("categoria do participante: ", tipoIngressoNome)
print ("valor do ingresso: R$", round(valorIngresso, 2))
print ("desconto: ", valorDesconto)
print ("valor total a pagar: R$", round(valorTotal, 2))