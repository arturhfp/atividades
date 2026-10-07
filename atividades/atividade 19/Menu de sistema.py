opcao = -1

while opcao != 0:
    print("\n1 - Cadastrar usuário")
    print("2 - Consultar usuário")
    print("3 - Alterar usuário")
    print("4 - Excluir usuário")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Operação selecionada: Cadastrar usuário.")
    elif opcao == 2:
        print("Operação selecionada: Consultar usuário.")
    elif opcao == 3:
        print("Operação selecionada: Alterar usuário.")
    elif opcao == 4:
        print("Operação selecionada: Excluir usuário.")
    elif opcao == 0:
        print("Saindo do sistema.")
    else:
        print("Opção inválida.")