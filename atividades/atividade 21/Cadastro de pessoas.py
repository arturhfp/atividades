"""Uma empresa precisa cadastrar os nomes de cinco pessoas que participarão de
um treinamento.
A lista deverá começar vazia. Cada nome informado deverá ser armazenado nela.
Estrutura que deve ser utilizada
Lista
A lista permite iniciar sem elementos e receber novos dados durante a execução
do programa.
O que desenvolver
1. Criar uma lista vazia.
2. Solicitar cinco nomes.
3. Adicionar cada nome à lista.
4. Apresentar os nomes cadastrados.
Resultado esperado
Exemplo:
Digite o nome: Ana
Digite o nome: Carlos
Digite o nome: Mariana
Digite o nome: Pedro
Digite o nome: João

Pessoas cadastradas:

Ana
Carlos
Mariana
Pedro
João"""

print("===================================================")
print("     [ N.E.R.V. - GEOPRONT SECURITY TERMINAL ]     ")
print("===================================================")
print("||                                               ||")
print("||                 G. E. H. I. R. A              ||")
print("||             [ system for training ]           ||")
print("||                                               ||")
print("===================================================")

pessoas = []

while True:
    print("\n1. Cadastrar pessoa")
    print("2. Listar pessoas cadastradas")
    print("3. adicionar pessoa")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if len(pessoas) >= 5:
            print("Limite de pessoas cadastradas atingido.")
            continue

        nome = input("Digite o nome: ")
        pessoas.append(nome)
        print(f"{nome} cadastrado com sucesso.")
    elif opcao == "2":
        print("\nPessoas cadastradas:\n")
        for pessoa in pessoas:
            print(f"o nome da pessoa é: {pessoa}")
    elif opcao == "3":
        if len(pessoas) >= 5:
            print("Limite de pessoas cadastradas atingido.")
            continue

        nome = input("Digite o nome: ")
        pessoas.append(nome)
        print(f"{nome} cadastrado com sucesso.")
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")