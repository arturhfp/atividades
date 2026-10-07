"""Um estacionamento possui 3 fileiras com 5 vagas em cada uma.
Uma matriz será utilizada para representar as vagas:
0 = vaga livre
1 = vaga ocupada
Exemplo:
estacionamento = [
[0, 1, 0, 0, 1],
[1, 1, 0, 1, 0],
[0, 0, 1, 0, 0]
]
Desenvolva um programa que:
• crie uma matriz 3 × 5;
• solicite ao usuário a situação de cada vaga;
• utilize append() para construir a matriz;

• apresente o estacionamento;
• conte quantas vagas estão ocupadas;
• conte quantas vagas estão livres.
Ao final, apresente:
Total de vagas: 15
Vagas ocupadas: 6
Vagas livres: 9"""


print("===================================================")
print("[ SISTEMA DE ESTACIONAMENTO - CONTROLE DE VAGAS ]  ")
print("===================================================")
print("||                                               ||")
print("||           PARK-FLOW AUTOMOTIVE SOLUTIONS      ||")
print("||             [ GESTÃO DE CATRACA E PÁTIO ]     ||")
print("||                                               ||")
print("||   STATUS: CANCELA ABERTA - VAGAS DISPONÍVEIS  ||")
print("===================================================")

estacionamento = []

for numero_fileira in range(1, 4):
    fileira = []
    print(f"\nInforme a situação das vagas da fileira {numero_fileira}.")

    for numero_vaga in range(1, 6):
        situacao = int(input(f"Vaga {numero_vaga} (0 livre, 1 ocupada): "))
        while situacao not in (0, 1):
            print("Opção inválida. Digite 0 para livre ou 1 para ocupada.")
            situacao = int(input(f"Vaga {numero_vaga} (0 livre, 1 ocupada): "))
        fileira.append(situacao)

    estacionamento.append(fileira)

print("\nESTACIONAMENTO")
for fileira in estacionamento:
    print(fileira)

vagas_ocupadas = sum(fileira.count(1) for fileira in estacionamento)
total_vagas = sum(len(fileira) for fileira in estacionamento)
vagas_livres = total_vagas - vagas_ocupadas

print(f"\nTotal de vagas: {total_vagas}")
print(f"Vagas ocupadas: {vagas_ocupadas}")
print(f"Vagas livres: {vagas_livres}")