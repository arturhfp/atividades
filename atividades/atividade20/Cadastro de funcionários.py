"""Uma empresa deseja armazenar informações básicas dos funcionários.
Cada funcionário deverá possuir:
• matrícula;
• nome;
• setor;
• cargo;
• salário.
Exemplo:
funcionario = {
"matricula": 1001,
"nome": "Carlos",
"setor": "Tecnologia",

"cargo": "Desenvolvedor",
"salario": 4500.00
}
Desenvolva um programa que:
• cadastre 5 funcionários;
• utilize uma lista para armazená-los;
• utilize append() para adicionar cada funcionário;
• ao final, apresente os funcionários cadastrados;
• solicite uma matrícula;
• localize o funcionário correspondente;
• apresente os dados encontrados.
A matrícula deverá funcionar como identificador único."""

print("===================================================")
print("[ TECH CORP - SOFTWARE ENGINEERING DIVISION ]     ")
print("===================================================")
print("||                                               ||")
print("||           NEXUS CODE TECHNOLOGIES             ||")
print("||             [ REPO: MASTER / DEPLOY ]         ||")
print("||                                               ||")
print("||   STATUS: KERNEL COMPILED & SERVERS ONLINE    ||")
print("===================================================")

funcionarios = []

while True:
    print("\n1 - Cadastro de funcionário")
    print("2 - Lista de funcionários")
    print("3 - Busca de funcionário")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        matricula = int(input("Matrícula: "))
        while any(
            funcionario["matricula"] == matricula
            for funcionario in funcionarios
        ):
            print("Essa matrícula já está cadastrada.")
            matricula = int(input("Informe outra matrícula: "))

        funcionario = {
            "matricula": matricula,
            "nome": input("Nome: "),
            "setor": input("Setor: "),
            "cargo": input("Cargo: "),
            "salario": float(input("Salário: "))
        }
        funcionarios.append(funcionario)
        print("Funcionário cadastrado com sucesso.")

    elif opcao == "2":
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
            continue

        print("\nFUNCIONÁRIOS CADASTRADOS")
        for funcionario in funcionarios:
            print(f"\nMatrícula: {funcionario['matricula']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Setor: {funcionario['setor']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: R$ {funcionario['salario']:.2f}")

    elif opcao == "3":
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
            continue

        matricula_busca = int(input("Digite a matrícula do funcionário: "))
        funcionario_encontrado = next(
            (
                funcionario for funcionario in funcionarios
                if funcionario["matricula"] == matricula_busca
            ),
            None
        )

        if funcionario_encontrado:
            print("\nFuncionário encontrado.")
            print(f"Matrícula: {funcionario_encontrado['matricula']}")
            print(f"Nome: {funcionario_encontrado['nome']}")
            print(f"Setor: {funcionario_encontrado['setor']}")
            print(f"Cargo: {funcionario_encontrado['cargo']}")
            print(f"Salário: R$ {funcionario_encontrado['salario']:.2f}")
        else:
            print("Funcionário não encontrado.")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 0.")
