clientes = {}


def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    clientes[cpf] = nome
    print("Cliente cadastrado com sucesso!")


def consultar_cliente():
    cpf = input("Digite o CPF do cliente: ")
    if cpf in clientes:
        print(f"Cliente: {clientes[cpf]}")
    else:
        print("Cliente não encontrado.")


def calcular_compra():
    preco = float(input("Digite o preço do produto: R$ "))
    quantidade = int(input("Digite a quantidade desejada: "))
    total = preco * quantidade
    print(f"O valor total da compra é R$ {total:.2f}")


def sair():
    print("Atendimento encerrado.")


while True:
    print("\nSistema de atendimento")
    print("1 - Cadastrar cliente")
    print("2 - Consultar cliente")
    print("3 - Calcular compra")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        consultar_cliente()
    elif opcao == "3":
        calcular_compra()
    elif opcao == "4":
        sair()
        break
    else:
        print("Opção inválida. Tente novamente..")
