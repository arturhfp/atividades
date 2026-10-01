print("temperatura local")

def converter_temperatura(temperaturaC):
    fahrenheit = (temperaturaC * 9 / 5) + 32
    return fahrenheit

temperaturaC = float(input("digite a temperatura: "))

fahrenheit = converter_temperatura(temperaturaC)

print(f"a temperatura em fahrenheit é : {fahrenheit}")