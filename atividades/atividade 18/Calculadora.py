print("calculadora")

def somador(num1, num2):
    soma = num1 + num2
    return soma


def subtrair(num1, num2):
    subtracao = num1 - num2
    return subtracao


def multiplicar(num1, num2):
    multiplicacao = num1 * num2
    return multiplicacao


def dividir(num1, num2):
    if num2 == 0:
        return "Erro: não é possível dividir por zero"
    divisao = num1 / num2
    return divisao


num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
operacao = input("selecione a operação: +, -, *, / ")

if operacao == "+":
    resultado = somador(num1, num2)
elif operacao == "-":
    resultado = subtrair(num1, num2)
elif operacao == "*":
    resultado = multiplicar(num1, num2)
elif operacao == "/":
    resultado = dividir(num1, num2)
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)

