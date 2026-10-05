"""Uma empresa precisa desenvolver um pequeno sistema para controlar seu
estoque.
Para cada produto, o sistema deverá armazenar:
• código do produto;
• nome;
• categoria;
• quantidade atual;
• quantidade mínima;
• preço.
Exemplo:
produto = {
"codigo": 101,
"nome": "Teclado",
"categoria": "Periféricos",
"quantidade": 15,
"quantidade_minima": 5,
"preco": 120.00
}
Desenvolva um programa que:

• crie uma lista vazia chamada estoque;
• permita cadastrar 5 produtos;
• solicite todas as informações ao usuário;
• utilize append() para armazenar cada produto;
• percorra os produtos cadastrados;
• apresente os dados de cada produto;
• informe quais produtos estão abaixo ou iguais à quantidade mínima.
Exemplo de resultado:
PRODUTOS QUE NECESSITAM DE REPOSIÇÃO

Código: 103
Produto: Mouse
Quantidade atual: 3
Quantidade mínima: 5
O código deverá ser utilizado como identificador do produto."""

print("===================================================")
print("[ SISTEMA DE CONTROLE DE ESTOQUE - LOGÍSTICA ]    ")
print("===================================================")
print("||                                               ||")
print("||           W. H. S. - WAREHOUSE HUB            ||")
print("||             [ INVENTÁRIO ATIVO ]              ||")
print("||                                               ||")
print("||   STATUS: ENTRADA E SAÍDA DE PRODUTOS OK      ||")
print("===================================================")

estoque = []

while True:
    print("\n1 - Cadastro de produto")
    print("2 - Estoque")
    print("3 - Produtos para reposição")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = int(input("Código do produto: "))
        while any(produto["codigo"] == codigo for produto in estoque):
            print("Esse código já está cadastrado.")
            codigo = int(input("Informe outro código: "))

        produto = {
            "codigo": codigo,
            "nome": input("Nome do produto: "),
            "categoria": input("Categoria: "),
            "quantidade": int(input("Quantidade atual: ")),
            "quantidade_minima": int(input("Quantidade mínima: ")),
            "preco": float(input("Preço: "))
        }
        estoque.append(produto)
        print("Produto cadastrado com sucesso.")

    elif opcao == "2":
        if not estoque:
            print("Nenhum produto cadastrado.")
            continue

        print("\nPRODUTOS CADASTRADOS")
        for produto in estoque:
            print(f"\nCódigo: {produto['codigo']}")
            print(f"Produto: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Quantidade atual: {produto['quantidade']}")
            print(f"Quantidade mínima: {produto['quantidade_minima']}")
            print(f"Preço: R$ {produto['preco']:.2f}")

    elif opcao == "3":
        reposicao = [
            produto for produto in estoque
            if produto["quantidade"] <= produto["quantidade_minima"]
        ]

        print("\nPRODUTOS QUE NECESSITAM DE REPOSIÇÃO")
        if reposicao:
            for produto in reposicao:
                print(f"\nCódigo: {produto['codigo']}")
                print(f"Produto: {produto['nome']}")
                print(f"Quantidade atual: {produto['quantidade']}")
                print(f"Quantidade mínima: {produto['quantidade_minima']}")
        else:
            print("Nenhum produto precisa de reposição.")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 0.")

