print ("Sistema de cálculo de frete")

nomecliente = input("digite o nome do cliente:")
valorCompra = float(input("digite o valor da compra: "))
pesoProduto = float(input("digite o peso do produto: "))
regiaoEntrega = int(input("digite a região de entrega (1 Região Metropolitana, 2 Interior do Estado, 3 Outros estados): "))
if regiaoEntrega == 1:
    regiaoEntregaNome = "Região Metropolitana"
    valorFrete = 12
elif regiaoEntrega == 2:
    regiaoEntregaNome = "Interior do Estado"
    valorFrete = 20
elif regiaoEntrega == 3:
    regiaoEntregaNome = "Outros estados"
    valorFrete = 35
else :
    print("opção inválida, digite 1, 2 ou 3")
    exit()
tipoEntrega = int(input("digite o tipo de entrega (1 Normal, 2 Expressa): "))
if tipoEntrega == 1:
    tipoEntregaNome = "Normal"
    valorFrete = valorFrete
elif tipoEntrega == 2:  
    tipoEntregaNome = "Expressa"
    valorFrete = valorFrete * 1.5
else:
    print("opção inválida, digite 1 ou 2") 
if valorCompra > 500:
    print("Parabéns! Você ganhou um desconto de 20% no frete.")
    valorFrete = valorFrete * 0.20
    print("O valor do frete com desconto é: R$", valorFrete)
if pesoProduto > 5:
    print("O peso do produto é maior que 5kg, havera um acrescimo de R$ 3,00 por peso excedente.")
    valorExcedente = (pesoProduto - 5) * 3
    valorFrete = valorFrete + valorExcedente
    print("O valor do frete com acrescimo é: R$", valorFrete)
else:
    print("O peso do produto é menor ou igual a 5kg, não havera acrescimo no frete.")

print("nome do cliente:", nomecliente)
print("valor da compra: R$", valorCompra)
print("peso do produto:", pesoProduto, "kg")
print("região de entrega:", regiaoEntregaNome)
print("tipo de entrega:", tipoEntregaNome)
print("valor do frete: R$", valorFrete)
print("valor total da compra com frete: R$", valorCompra + valorFrete)
    
        