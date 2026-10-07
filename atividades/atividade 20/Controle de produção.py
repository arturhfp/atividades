"""Uma indústria precisa registrar a quantidade de produtos fabricados por
diferentes máquinas durante os dias da semana.
Considere:
• 3 máquinas;
• 5 dias de produção.
Utilize uma matriz para representar os dados.
Cada linha deverá representar uma máquina e cada coluna um dia da semana.
Exemplo:
producao = [
[120, 135, 140, 150, 145],
[100, 110, 125, 130, 128],
[150, 160, 155, 170, 180]
]
Desenvolva um programa que:
• permita informar a produção de cada máquina durante os 5 dias;
• utilize append() para construir a matriz;
• apresente a produção organizada por máquina;
• calcule o total produzido por cada máquina;
• calcule o total produzido pela indústria;
• identifique qual máquina produziu a maior quantidade durante a semana.
Ao final, apresente um relatório semelhante a:
===== PRODUÇÃO SEMANAL =====

Máquina 1: 690 unidades
Máquina 2: 593 unidades
Máquina 3: 815 unidades

Total produzido: 2098 unidades

Máquina com maior produção: Máquina 3"""




producao = []

for numero_maquina in range(1, 4):
    producao_maquina = []
    print(f"\nProdução da máquina {numero_maquina}")

    for dia in range(1, 6):
        quantidade = int(input(f"Quantidade produzida no dia {dia}: "))
        producao_maquina.append(quantidade)

    producao.append(producao_maquina)

print("\n===== PRODUÇÃO SEMANAL =====")

totais_por_maquina = []
for numero_maquina, producao_maquina in enumerate(producao, start=1):
    total_maquina = sum(producao_maquina)
    totais_por_maquina.append(total_maquina)
    print(f"\nMáquina {numero_maquina}")
    print(f"Produção diária: {producao_maquina}")
    print(f"Total: {total_maquina} unidades")

total_industria = sum(totais_por_maquina)
maquina_maior_producao = totais_por_maquina.index(max(totais_por_maquina)) + 1

print(f"\nTotal produzido: {total_industria} unidades")
print(f"\nMáquina com maior produção: Máquina {maquina_maior_producao}")

