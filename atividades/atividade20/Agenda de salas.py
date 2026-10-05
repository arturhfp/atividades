"""Uma empresa possui 3 salas de reunião e precisa controlar a utilização durante 4
períodos do dia.
Considere:
0 = disponível
1 = ocupado
A matriz deverá representar:
• cada linha → uma sala;
• cada coluna → um período.
Exemplo:
salas = [
[0, 1, 0, 0],
[1, 0, 1, 0],
[0, 0, 1, 1]
]
Desenvolva um programa que:
• crie a matriz;
• permita ao usuário informar a situação de cada sala e período;
• apresente a matriz;
• solicite uma sala e um período;

• informe se o horário está disponível ou ocupado.
Também informe quantos horários estão disponíveis em cada sala."""

print("===================================================")
print("[ CORPORATE HQ - BUSINESS MANAGEMENT DIVISION ]   ")
print("===================================================")
print("||                                               ||")
print("||           APEX GLOBAL ENTERPRISES             ||")
print("||             [ FINANCIAL & STRATEGY ]          ||")
print("||                                               ||")
print("||   STATUS: Q4 PERFORMANCE & ASSETS SECURED     ||")
print("===================================================")

salas = [[0, 0, 0, 0] for _ in range(3)]

while True:
    print("\n1 - Agendar sala")
    print("2 - Conferir salas")
    print("3 - Situação da sala")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        sala = int(input("Digite o número da sala (1 a 3): "))
        while sala not in range(1, 4):
            print("Sala inválida. Escolha um número de 1 a 3.")
            sala = int(input("Digite o número da sala (1 a 3): "))

        periodo = int(input("Digite o número do período (1 a 4): "))
        while periodo not in range(1, 5):
            print("Período inválido. Escolha um número de 1 a 4.")
            periodo = int(input("Digite o número do período (1 a 4): "))

        if salas[sala - 1][periodo - 1] == 0:
            salas[sala - 1][periodo - 1] = 1
            print(f"Sala {sala}, período {periodo} agendado com sucesso.")
        else:
            print(f"Sala {sala}, período {periodo} já está ocupado.")

    elif opcao == "2":
        print("\nAGENDA DAS SALAS")
        for numero_sala, periodos in enumerate(salas, start=1):
            print(f"Sala {numero_sala}: {periodos}")
            print(f"Horários disponíveis: {periodos.count(0)}")

    elif opcao == "3":
        sala = int(input("Digite o número da sala (1 a 3): "))
        while sala not in range(1, 4):
            print("Sala inválida. Escolha um número de 1 a 3.")
            sala = int(input("Digite o número da sala (1 a 3): "))

        periodo = int(input("Digite o número do período (1 a 4): "))
        while periodo not in range(1, 5):
            print("Período inválido. Escolha um número de 1 a 4.")
            periodo = int(input("Digite o número do período (1 a 4): "))

        if salas[sala - 1][periodo - 1] == 0:
            print(f"Sala {sala}, período {periodo}: horário disponível.")
        else:
            print(f"Sala {sala}, período {periodo}: horário ocupado.")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 0.")
