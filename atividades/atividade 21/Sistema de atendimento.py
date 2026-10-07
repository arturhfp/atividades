"""Uma empresa precisa desenvolver um pequeno sistema para controlar o
atendimento de clientes.
O sistema deverá permitir que clientes sejam adicionados à fila e atendidos na
ordem em que chegaram.
Enquanto houver clientes aguardando, o sistema deverá continuar realizando os
atendimentos.
Estrutura que deve ser utilizada
Fila
A fila deve ser utilizada porque o atendimento precisa respeitar a ordem de
chegada dos clientes.

O que desenvolver
O sistema deverá:
1. Criar uma fila vazia.
2. Adicionar cinco clientes.
3. Exibir os clientes aguardando.
4. Atender o primeiro cliente.
5. Remover o cliente atendido.
6. Exibir quantos clientes ainda aguardam.
7. Continuar o atendimento utilizando while.
8. Encerrar quando a fila estiver vazia.
Resultado esperado
Clientes aguardando:

Ana
Carlos
Mariana
Pedro
João

Atendendo: Ana
Clientes restantes: 4

Atendendo: Carlos
Clientes restantes: 3

Atendendo: Mariana
Clientes restantes: 2

Atendendo: Pedro
Clientes restantes: 1

Atendendo: João
Clientes restantes: 0

Fila vazia.
Todos os clientes foram atendidos."""

print("===================================================")
print("[AUTO PEÇAS & LUBRIFICANTES  MANUTENÇÃO AUTOMOTIVA]")
print("===================================================")
print("||                                               ||")
print("||           CENTRAL DE PEÇAS & ÓLEOS            ||")
print("||        [ FILTROS, ADITIVOS & COMPONENTES ]    ||")
print("||                                               ||")
print("||   STATUS: ESTOQUE DE PEÇAS E TROCA DE ÓLEO OK ||")
print("===================================================")

clientes = []

while True:
    print("\n1. Adicionar cliente")
    print("2. Listar clientes na fila")
    print("3. Atender cliente")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input ("Digite o nome do cliente: ")
        clientes.append(nome)
        print(f"{nome} adicionado à fila de atendimento.")
    elif opcao == "2":
        print("\nClientes aguardando:\n")
        for cliente in clientes:
            print(cliente)
    elif opcao == "3":
        if clientes:
            cliente_atendido = clientes.pop(0)
            print(f"Atendendo: {cliente_atendido}")
            print(f"Clientes restantes: {len(clientes)}")
        else:
            print("Não há clientes na fila.")
    elif opcao == "4":
        break