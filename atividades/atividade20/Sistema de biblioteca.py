"""Uma biblioteca precisa controlar os livros disponíveis para empréstimo.
Cada livro deverá possuir:
• código;
• título;
• autor;
• ano de publicação;
• quantidade disponível.
Desenvolva um programa que:
• crie uma lista chamada livros;
• cadastre 4 livros;
• utilize append() para armazenar cada livro;

• apresente todos os livros cadastrados;
• solicite um código de livro;
• procure o livro pelo código;
• apresente suas informações caso seja encontrado.
Exemplo:
Digite o código do livro: 203

Livro encontrado.

Título: Introdução à Programação
Autor: João Silva
Ano: 2025
Quantidade disponível: 3
A busca deverá ser realizada pelo código, e não pelo título."""

print("===================================================")
print("[ SISTEMA DE BIBLIOTECA - GERENCIAMENTO DE ACERVO ]")
print("===================================================")
print("||                                               ||")
print("||           BIBLIOTECA CENTRAL ALEXANDRIA       ||")
print("||             [ CATALOGAÇÃO DE LIVROS ]         ||")
print("||                                               ||")
print("||   STATUS: EMPRÉSTIMOS E DEVOLUÇÕES LIBERADOS  ||")
print("===================================================")

livros = []

while True:
    print("\n1 - Cadastrar livro")
    print("2 - Consultar livros")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = int(input("Código: "))
        while any(livro["codigo"] == codigo for livro in livros):
            print("Esse código já está cadastrado.")
            codigo = int(input("Informe outro código: "))

        livro = {
            "codigo": codigo,
            "titulo": input("Título: "),
            "autor": input("Autor: "),
            "ano": int(input("Ano de publicação: ")),
            "quantidade": int(input("Quantidade disponível: "))
        }
        livros.append(livro)
        print("Livro cadastrado com sucesso.")

    elif opcao == "2":
        if not livros:
            print("Nenhum livro cadastrado.")
            continue

        print("\nLIVROS CADASTRADOS")
        for livro in livros:
            print(f"\nCódigo: {livro['codigo']}")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Quantidade disponível: {livro['quantidade']}")

        codigo_busca = int(input("\nDigite o código do livro para consultar: "))
        livro_encontrado = next(
            (livro for livro in livros if livro["codigo"] == codigo_busca),
            None
        )

        if livro_encontrado:
            print("\nLivro encontrado.")
            print(f"Título: {livro_encontrado['titulo']}")
            print(f"Autor: {livro_encontrado['autor']}")
            print(f"Ano: {livro_encontrado['ano']}")
            print(f"Quantidade disponível: {livro_encontrado['quantidade']}")
        else:
            print("\nLivro não encontrado.")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha 1, 2 ou 0.")
