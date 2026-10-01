

def calcular_desconto(compra):
    if compra <= 100:
        return compra
    elif compra > 100 and compra <= 500: 
        return compra * 0.10
    elif compra > 500 : 
            return compra * 0.15


compra = float(input("preço: "))
valortotal = compra - calcular_desconto(compra)    



print(f"o valor total é: {valortotal:.2f}")