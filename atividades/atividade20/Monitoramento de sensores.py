"""Uma empresa utiliza sensores para monitorar a temperatura de diferentes
ambientes.
Existem:
• 3 ambientes;
• 4 sensores em cada ambiente.
Utilize uma matriz para armazenar as temperaturas.
Exemplo:
temperaturas = [
[22.5, 23.1, 22.8, 24.0],
[25.2, 26.0, 25.5, 24.8],
[20.5, 21.0, 20.8, 21.5]
]
Desenvolva um programa que:
• solicite as temperaturas;
• construa a matriz utilizando append();
• apresente a matriz;
• calcule a média de cada ambiente;
• identifique a maior temperatura registrada;
• identifique a menor temperatura registrada.
Ao final, apresente os resultados organizados por ambiente."""

temperaturas = []

for numero_ambiente in range(1, 4):
    leituras = []
    print(f"\nAmbiente {numero_ambiente}")

    for numero_sensor in range(1, 5):
        temperatura = float(
            input(f"Temperatura do sensor {numero_sensor}: ")
        )
        leituras.append(temperatura)

    temperaturas.append(leituras)

print("\nRESULTADOS DO MONITORAMENTO")
for numero_ambiente, leituras in enumerate(temperaturas, start=1):
    media = sum(leituras) / len(leituras)
    print(f"\nAmbiente {numero_ambiente}")
    print(f"Temperaturas: {leituras}")
    print(f"Média: {media:.2f} °C")

maior_temperatura = max(max(leituras) for leituras in temperaturas)
menor_temperatura = min(min(leituras) for leituras in temperaturas)

print(f"\nMaior temperatura registrada: {maior_temperatura:.2f} °C")
print(f"Menor temperatura registrada: {menor_temperatura:.2f} °C")