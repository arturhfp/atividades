'''Um laboratório de informática precisa manter o controle dos equipamentos
disponíveis.
Cada equipamento possui informações diferentes e, por isso, o sistema deverá
armazenar um conjunto de dados para cada equipamento.
Para cada equipamento, deverão ser armazenados:
• código do equipamento;
• nome;
• tipo;
• quantidade;
• situação.
Exemplo:
equipamento = {
"codigo": 101,
"nome": "Computador Dell",
"tipo": "Desktop",
"quantidade": 20,
"situacao": "Disponível"
}
Desenvolva um programa que:

• crie uma lista vazia chamada equipamentos;
• cadastre 3 equipamentos;
• solicite todas as informações ao usuário;
• utilize um dicionário para representar cada equipamento;
• utilize append() para adicionar cada equipamento à lista;
• ao final, percorra a lista e apresente todos os equipamentos cadastrados.
O código deverá funcionar como identificador do equipamento.'''




print("===================================================")
print("[ N.E.R.V. - GEOPRONT SECURITY TERMINAL ]         ")
print("===================================================")
print("||                                               ||")
print("||                 G. E. H. I. R. A             ||")
print("||             [ MAGI SYSTEM: MELCHIOR ]         ||")
print("||                                               ||")
print("||   GOD'S IN HIS HEAVEN. ALL'S RIGHT WITH THE WORLD.||")
print("===================================================")


equipamentos = []

if __name__ == "__main__":
    print("Bem-vindo ao sistema de cadastro de equipamentos do laboratório da NERV")
    while True:
        print("\n1 - Cadastrar equipamento")
        print("2 - Consultar equipamento")
        print("3 - Listar equipamentos")
        print("4 - Alterar disponibilidade")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo_base = input("Digite o código do equipamento/lote: ").strip()
            if any(eq["codigo_base"] == codigo_base for eq in equipamentos):
                print("Esse código já está cadastrado.")
                continue

            nome = input("Digite o nome do equipamento: ").strip()
            tipo = input("Digite o tipo do equipamento: ").strip()
            try:
                quantidade = int(input("Digite a quantidade: "))
                if quantidade < 1:
                    print("A quantidade deve ser maior que zero.")
                    continue
            except ValueError:
                print("Digite uma quantidade válida.")
                continue

            for numero in range(1, quantidade + 1):
                equipamento = {
                    "codigo": f"{codigo_base}-{numero:02}",
                    "codigo_base": codigo_base,
                    "nome": nome,
                    "tipo": tipo,
                    "quantidade": 1,
                    "situacao": "Disponível",
                }
                equipamentos.append(equipamento)
            print(f"{quantidade} unidade(s) cadastrada(s) com sucesso!")

        elif opcao == "2":
            codigo_consulta = input("Digite o código do lote ou da unidade: ").strip()
            encontrados = [
                eq for eq in equipamentos
                if eq["codigo"] == codigo_consulta or eq["codigo_base"] == codigo_consulta
            ]
            if encontrados:
                for eq in encontrados:
                    print(f"Código: {eq['codigo']} | {eq['nome']} ({eq['tipo']}) | {eq['situacao']}")
            else:
                print("Equipamento não encontrado.")

        elif opcao == "3":
            print("Lista de equipamentos cadastrados:")
            if not equipamentos:
                print("Nenhum equipamento cadastrado.")
            for eq in equipamentos:
                print(f"Código: {eq['codigo']} | {eq['nome']} ({eq['tipo']}) | {eq['situacao']}")

        elif opcao == "4":
            codigo_unidade = input("Digite o código da unidade (ex.: D01-02): ").strip()
            equipamento_encontrado = None
            for eq in equipamentos:
                if eq["codigo"] == codigo_unidade:
                    equipamento_encontrado = eq
                    break

            if equipamento_encontrado is None:
                print("Unidade não encontrada.")
                continue

            print("1 - Disponível")
            print("2 - Indisponível")
            situacao = input("Nova situação: ")
            if situacao == "1":
                equipamento_encontrado["situacao"] = "Disponível"
            elif situacao == "2":
                equipamento_encontrado["situacao"] = "Indisponível"
            else:
                print("Opção inválida. A situação não foi alterada.")
                continue
            print("Situação atualizada com sucesso.")

        elif opcao == "5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")
