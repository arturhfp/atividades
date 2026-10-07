"""Uma biblioteca possui uma pilha de livros sobre uma mesa.
Um novo livro é colocado sempre sobre o último livro que foi colocado. Quando
um livro precisa ser retirado, o livro que está no topo deve sair primeiro.

Estrutura que deve ser utilizada
Pilha
A pilha utiliza o princípio LIFO — Last In, First Out, em que o último elemento
inserido é o primeiro a ser retirado.
O que desenvolver
1. Criar uma pilha.
2. Adicionar cinco livros.
3. Retirar os livros utilizando pop().
4. Utilizar while até que a pilha fique vazia.
Resultado esperado
Se os livros forem adicionados nesta ordem:
Livro 1
Livro 2
Livro 3
Livro 4
Livro 5
A retirada deverá ocorrer assim:
Retirando: Livro 5
Retirando: Livro 4
Retirando: Livro 3
Retirando: Livro 2
Retirando: Livro 1"""

livros = []

print("\n===================================================")
print("        [ BIBLIOTECA - PILHA DE LIVROS ]           ")
print("===================================================")

print("\n1 - Adicionar livros à pilha")
print("2 - Retirar livros da pilha")

while True:
    opcao = input("\nEscolha uma opção (1 ou 2): ")
    if opcao == "1":
        for i in range(5):
            livro = input(f"Digite o nome do livro {i + 1}: ")
            livros.append(livro)
            print(f"{livro} adicionado à pilha.")
    elif opcao == "2":
        print("\nRetirando livros da pilha:\n")
        while livros:
            livro_retirado = livros.pop()
            print(f"Retirando: {livro_retirado}")
        print("Todos os livros foram retirados da pilha.")
        break
    else:
        print("Opção inválida. Tente novamente.")