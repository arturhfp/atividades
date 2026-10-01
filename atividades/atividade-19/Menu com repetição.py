print("===================================================")
print("[ SISTEMA ESCOLAR - SECRETARIA ACADÊMICA ]       ")
print("===================================================")
print("||                                               ||")
print("||           INSTITUTO EDUCACIONAL TOKYO         ||")
print("||             [ MATRÍCULAS 2026 ]               ||")
print("||                                               ||")
print("||   STATUS: VALIDAÇÃO DE DADOS DE ALUNOS        ||")
print("===================================================")

alunos = []
notas = []

opcao = -1

while opcao != 0:
    print("\n1 - Cadastrar alunos")
    print("2 - Consultar alunos")
    print("3 - Cadastrar notas")
    print("4 - Quantidade de alunos")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
            print(f"\n[ ALUNO]")
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))

            aluno = {
                "nome": nome,
                "idade": idade,
            }
            alunos.append(aluno)
    elif opcao == 2:
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("\n=== Lista de alunos cadastrados ===")
            for aluno in alunos:
                print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}")
    elif opcao == 3:
        if not alunos:
            print("Cadastre os alunos antes de registrar as notas.")
        else:
            for aluno in alunos:
                print(f"\n[ NOTAS DO ALUNO {aluno['nome']} ]")
                nota1 = float(input("Digite a primeira nota do aluno: "))
                notas.append({
                    "aluno": aluno["nome"],
                    "nota1": nota1,
                })
    elif opcao == 4:
        print("\n=== Quantidade de alunos cadastrados ===")
        print(f"Total de alunos: {len(alunos)}")
    elif opcao == 0:
        print("Saindo do sistema.")
    else:
        print("Opção inválida. Escolha uma opção do menu.")

                        