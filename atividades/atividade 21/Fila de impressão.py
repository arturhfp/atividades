"""Uma empresa possui vários documentos aguardando impressão.
Os documentos devem ser impressos na ordem em que foram enviados para a
impressora. Um documento que chegou depois não pode ser impresso antes dos
documentos que já estavam aguardando.
Estrutura que deve ser utilizada
Fila
A fila representa corretamente o funcionamento de uma impressora, pois o
primeiro documento enviado deve ser processado primeiro.
O que desenvolver
Adicione os seguintes documentos:
Relatório
Contrato
Currículo
Nota Fiscal
Planilha
Depois, utilize um while para processar os documentos até que a fila fique vazia.
Resultado esperado
Imprimindo: Relatório
Imprimindo: Contrato
Imprimindo: Currículo
Imprimindo: Nota Fiscal
Imprimindo: Planilha

Todos os documentos foram impressos."""


impressora = ["Relatório", "Contrato", "Currículo", "Nota Fiscal", "Planilha"]

while True:
    print("1. Listar documentos na fila")
    print("2. Imprimir documento")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("\nFila de impressão:\n")
        for documento in impressora:
            print(documento)
    elif opcao == "2":
        if impressora:
            documento_impresso = impressora.pop(0)
            print(f"Imprimindo: {documento_impresso}")
        else:
            print("Não há documentos na fila.")
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")