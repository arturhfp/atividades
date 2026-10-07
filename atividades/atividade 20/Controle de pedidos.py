"""Uma empresa deseja armazenar os pedidos realizados pelos clientes.
Cada pedido deverá possuir:
• número do pedido;
• nome do cliente;
• produto;
• quantidade;
• valor unitário;
• situação.
Exemplo:
pedido = {
"numero": 1001,
"cliente": "Mariana",
"produto": "Mouse",
"quantidade": 2,
"valor_unitario": 45.00,
"situacao": "Em preparação"
}
Desenvolva um programa que:
• cadastre 5 pedidos;
• utilize uma lista para armazená-los;
• utilize append();
• calcule o valor total de cada pedido;
• apresente todos os pedidos;
• solicite o número de um pedido;
• localize o pedido pelo número;
• apresente todas as informações do pedido encontrado.
O número do pedido deverá ser utilizado como identificador."""

pedidos = []

while True:
    print("\n1 - Cadastrar pedido")
    print("2 - Consultar pedido")
    print("3 - Listar números e valores totais dos pedidos")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = int(input("Número do pedido: "))
        while any(pedido["numero"] == numero for pedido in pedidos):
            print("Esse número de pedido já está cadastrado.")
            numero = int(input("Informe outro número: "))

        pedido = {
            "numero": numero,
            "cliente": input("Nome do cliente: "),
            "produto": input("Produto: "),
            "quantidade": int(input("Quantidade: ")),
            "valor_unitario": float(input("Valor unitário: ")),
            "situacao": input("Situação: ")
        }
        pedido["valor_total"] = pedido["quantidade"] * pedido["valor_unitario"]
        pedidos.append(pedido)
        print("Pedido cadastrado com sucesso.")

    elif opcao == "2":
        if not pedidos:
            print("Nenhum pedido cadastrado.")
            continue

        numero_busca = int(input("Digite o número do pedido: "))
        pedido_encontrado = next(
            (pedido for pedido in pedidos if pedido["numero"] == numero_busca),
            None
        )

        if pedido_encontrado:
            print("\nPedido encontrado.")
            print(f"Número do pedido: {pedido_encontrado['numero']}")
            print(f"Cliente: {pedido_encontrado['cliente']}")
            print(f"Produto: {pedido_encontrado['produto']}")
            print(f"Quantidade: {pedido_encontrado['quantidade']}")
            print(f"Valor unitário: R$ {pedido_encontrado['valor_unitario']:.2f}")
            print(f"Valor total: R$ {pedido_encontrado['valor_total']:.2f}")
            print(f"Situação: {pedido_encontrado['situacao']}")
        else:
            print("Pedido não encontrado.")

    elif opcao == "3":
        if not pedidos:
            print("Nenhum pedido cadastrado.")
            continue

        print("\nNÚMERO E VALOR TOTAL DOS PEDIDOS")
        for pedido in pedidos:
            print(
                f"Pedido {pedido['numero']}: "
                f"R$ {pedido['valor_total']:.2f}"
            )

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 0.")