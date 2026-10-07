print("CALCULADORA")

numero1 = float(input("Digite o primeiro número: "))
operacao = input("Escolha a operação (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = numero1 + numero2

elif operacao == "-":
    resultado = numero1 - numero2

elif operacao == "*":
    resultado = numero1 * numero2

elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro: não é possível dividir por zero.")
        exit()

else:
    print("Erro: operação inválida.")
    exit()

print(f"Resultado: {resultado:.2f}")
#teste