"""Uma empresa possui uma frota de veículos e precisa controlar seus dados.
Cada veículo deverá possuir:
• código;
• placa;
• modelo;
• marca;
• ano;
• quilometragem;
• situação.
Exemplo:
veiculo = {
"codigo": 1,
"placa": "ABC1D23",
"modelo": "Onix",
"marca": "Chevrolet",
"ano": 2024,
"quilometragem": 35000,
"situacao": "Disponível"
}
Desenvolva um programa que:
• cadastre 4 veículos;
• armazene os veículos em uma lista;
• utilize append();
• apresente todos os veículos;

• solicite uma placa;
• localize o veículo pela placa;
• apresente seus dados.
Ao final, informe também qual veículo possui a maior quilometragem."""

print("===================================================")
print("[ AUTOMOTIVE CORP - VEHICLE MANUFACTURING DIVISION ]")
print("===================================================")
print("||                                               ||")
print("||           NEXUS MOTORS & ASSEMBLY             ||")
print("||             [ LINHA DE MONTAGEM / QA ]        ||")
print("||                                               ||")
print("||   STATUS: MOTOR TESTED & VEHICLE READY FOR ROAD ||")
print("===================================================")

veiculos = []

while True:
    print("\n1 - Cadastrar veículo")
    print("2 - Lista de veículos")
    print("3 - Localizar veículo pela placa")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nCadastro de veículo")

        codigo = int(input("Código: "))
        while any(veiculo["codigo"] == codigo for veiculo in veiculos):
            print("Esse código já está cadastrado.")
            codigo = int(input("Informe outro código: "))

        placa = input("Placa: ").strip().upper()
        while any(veiculo["placa"] == placa for veiculo in veiculos):
            print("Essa placa já está cadastrada.")
            placa = input("Informe outra placa: ").strip().upper()

        veiculo = {
            "codigo": codigo,
            "placa": placa,
            "modelo": input("Modelo: "),
            "marca": input("Marca: "),
            "ano": int(input("Ano: ")),
            "quilometragem": float(input("Quilometragem: ")),
            "situacao": input("Situação: ")
        }
        veiculos.append(veiculo)
        print("Veículo cadastrado com sucesso.")

    elif opcao == "2":
        if not veiculos:
            print("Nenhum veículo cadastrado.")
            continue

        print("\nVEÍCULOS CADASTRADOS")
        for veiculo in veiculos:
            print(f"\nCódigo: {veiculo['codigo']}")
            print(f"Placa: {veiculo['placa']}")
            print(f"Modelo: {veiculo['modelo']}")
            print(f"Marca: {veiculo['marca']}")
            print(f"Ano: {veiculo['ano']}")
            print(f"Quilometragem: {veiculo['quilometragem']:g} km")
            print(f"Situação: {veiculo['situacao']}")

        veiculo_mais_rodado = max(
            veiculos, key=lambda item: item["quilometragem"]
        )
        print("\nVEÍCULO COM MAIOR QUILOMETRAGEM")
        print(f"Placa: {veiculo_mais_rodado['placa']}")
        print(f"Modelo: {veiculo_mais_rodado['modelo']}")
        print(f"Quilometragem: {veiculo_mais_rodado['quilometragem']:g} km")

    elif opcao == "3":
        if not veiculos:
            print("Nenhum veículo cadastrado.")
            continue

        placa_busca = input("Digite a placa do veículo: ").strip().upper()
        veiculo_encontrado = next(
            (veiculo for veiculo in veiculos if veiculo["placa"] == placa_busca),
            None
        )

        if veiculo_encontrado:
            print("\nVeículo encontrado.")
            print(f"Código: {veiculo_encontrado['codigo']}")
            print(f"Placa: {veiculo_encontrado['placa']}")
            print(f"Modelo: {veiculo_encontrado['modelo']}")
            print(f"Marca: {veiculo_encontrado['marca']}")
            print(f"Ano: {veiculo_encontrado['ano']}")
            print(f"Quilometragem: {veiculo_encontrado['quilometragem']:g} km")
            print(f"Situação: {veiculo_encontrado['situacao']}")
        else:
            print("Veículo não encontrado.")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 0.")
