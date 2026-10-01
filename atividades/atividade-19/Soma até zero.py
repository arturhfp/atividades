soma = 0
numero = float(input("Digite um número (0 para encerrar): "))

while numero != 0:
    soma += numero
    numero = float(input("Digite outro número (0 para encerrar): "))

print(f"Soma dos valores informados: {soma}")