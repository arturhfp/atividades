print ("compra de produto")

def calcular_total(preco,quantia):
    totalVenda = preco * quantia
    return totalVenda

nomeProduto = input("digite o nome do produto: ")
preco = float(input("digite o preço do produto: "))
quantia = float(input("digite a quantia desejada: "))

totalVenda = calcular_total(preco,quantia)

print (f"o total da sua compra foi R${totalVenda} sendo {quantia} {nomeProduto}s")