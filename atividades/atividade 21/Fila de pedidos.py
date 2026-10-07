"""Uma empresa de alimentação possui pedidos aguardando preparação.

Os pedidos precisam ser preparados na ordem em que foram recebidos para
evitar que um pedido mais recente seja processado antes de outro que está
esperando há mais tempo.
Estrutura que deve ser utilizada
Fila
A fila permite processar os pedidos seguindo a ordem de chegada.
O que desenvolver
Cadastre cinco pedidos e depois processe todos utilizando um while.
Resultado esperado
Pedidos aguardando:

Pedido 1
Pedido 2
Pedido 3
Pedido 4
Pedido 5

Processando Pedido 1
Processando Pedido 2
Processando Pedido 3
Processando Pedido 4
Processando Pedido 5

Todos os pedidos foram processados."""


pedidos = []

while True:
    print ("\n1. Adicionar pedido")
    print ("2. Listar pedidos na fila")
    print ("3. Processar pedido")
    print ("4. Sair")
    opcao = input("escolha uma opcao: ")
    if opcao == "1":
        import random
        from datetime import datetime

        nomeCLiente = input("Digite o nome do cliente: ")
        produto = input("Digite o produto: ")

        # Pega a data atual no formato brasileiro (DD/MM/AAAA)
        data_atual = datetime.now().strftime("%d/%m/%Y")

        # Gera um número aleatório de 4 dígitos (de 1000 a 9999 para ficar com tamanho padrão)
        aleatorio = random.randint(1000, 9999)

        # Junta tudo em um código de pedido
        codigo_pedido = f"PED-{data_atual}-{aleatorio}"

        print(codigo_pedido)
        # Exemplo de saída: PED-07/10/2026-4829
        pedidos.append(codigo_pedido)
    elif opcao == "2":
        print("\nPedidos aguardando:\n")
        for pedido in pedidos:
            print(pedido)

    elif opcao == "3":
        if pedidos:
            pedido_processado = pedidos.pop(0)
            print(f"Processando {pedido_processado}")
            if not pedidos:
                print("Todos os pedidos foram processados.")
        else:
            print("Não há pedidos na fila.")
