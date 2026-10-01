print("maior numero")

def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "os numeros são iguais"

num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))

maior = maior_numero(num1, num2)

print("O maior número é:", maior)


