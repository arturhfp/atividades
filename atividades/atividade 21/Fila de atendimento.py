"""Uma clínica precisa controlar o atendimento dos pacientes.
Os pacientes devem ser atendidos na mesma ordem em que chegaram. O
primeiro paciente que chegou deve ser o primeiro a ser atendido.
Estrutura que deve ser utilizada
Fila
A fila é adequada porque utiliza o princípio FIFO — First In, First Out.
O que desenvolver
1. Criar uma fila.
2. Adicionar cinco pacientes.
3. Apresentar a fila.
4. Atender os pacientes um por vez.
5. Retirar o primeiro paciente da fila a cada atendimento.
Resultado esperado
Fila de atendimento:
Ana
Carlos
Mariana
Pedro
João

Atendendo: Ana
Atendendo: Carlos
Atendendo: Mariana
Atendendo: Pedro
Atendendo: João"""


print("===================================================")
print("        [ S.U.S. - SISTEMA ÚNICO DE SAÚDE ]        ")
print("===================================================")
print("||                                               ||")
print("||         MINISTÉRIO DA SAÚDE - BRASIL          ||")
print("||     [ SAÚDE PÚBLICA DE ACESSO UNIVERSAL ]     ||")
print("||                                               ||")
print("||   STATUS: ATENDIMENTO E CARTÃO SUS ATIVOS     ||")
print("===================================================")

pacientes = []

while True:
    print("\n1. Adicionar paciente")
    print("2. Listar pacientes na fila")
    print("3. Atender paciente")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input ("Digite o nome do paciente: ")
        pacientes.append(nome)
        print(f"{nome} adicionado à fila de atendimento.")
    elif opcao == "2":
        print("\nFila de atendimento:\n")
        for paciente in pacientes:
            print(paciente)
    elif opcao == "3":
        if pacientes:
            paciente_atendido = pacientes.pop(0)
            print(f"Atendendo: {paciente_atendido}")
        else:
            print("Não há pacientes na fila.")
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")