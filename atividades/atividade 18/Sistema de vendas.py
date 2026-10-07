compra = {
	"produto": "",
	"preco": 0.0,
	"quantidade": 0,
	"subtotal": 0.0,
	"desconto": 0.0,
	"pagamento": 0.0,
}


def cadastrar_produto():
	compra["produto"] = input("Digite o nome do produto: ")
	compra["preco"] = float(input("Digite o preço do produto: R$ "))
	compra["quantidade"] = int(input("Digite a quantidade: "))
	compra["subtotal"] = 0.0
	compra["desconto"] = 0.0
	compra["pagamento"] = 0.0
	print("Produto cadastrado com sucesso!")


def calcular_subtotal():
	if not compra["produto"]:
		print("Cadastre um produto antes de calcular o subtotal.")
		return

	compra["subtotal"] = compra["preco"] * compra["quantidade"]
	print(f"Subtotal: R$ {compra['subtotal']:.2f}")


def aplicar_desconto():
	if compra["subtotal"] == 0:
		print("Calcule o subtotal antes de aplicar o desconto.")
		return

	if compra["subtotal"] > 500:
		compra["desconto"] = compra["subtotal"] * 0.15
	elif compra["subtotal"] > 100:
		compra["desconto"] = compra["subtotal"] * 0.10
	else:
		compra["desconto"] = 0.0

	print(f"Desconto: R$ {compra['desconto']:.2f}")


def calcular_pagamento():
	if compra["subtotal"] == 0:
		print("Calcule o subtotal antes de calcular o pagamento.")
		return

	compra["pagamento"] = compra["subtotal"] - compra["desconto"]
	print(f"Valor a pagar: R$ {compra['pagamento']:.2f}")


def exibir_resumo():
	if not compra["produto"]:
		print("Ainda não há produto cadastrado.")
		return

	print("\nResumo da compra")
	print(f"Produto: {compra['produto']}")
	print(f"Preço unitário: R$ {compra['preco']:.2f}")
	print(f"Quantidade: {compra['quantidade']}")
	print(f"Subtotal: R$ {compra['subtotal']:.2f}")
	print(f"Desconto: R$ {compra['desconto']:.2f}")
	print(f"Valor final: R$ {compra['pagamento']:.2f}")


def sair():
	print("Sistema encerrado.")


while True:
	print("\nSistema de vendas")
	print("1 - Cadastrar produto")
	print("2 - Calcular subtotal")
	print("3 - Aplicar desconto")
	print("4 - Calcular pagamento")
	print("5 - Exibir resumo da compra")
	print("0 - Sair")

	opcao = input("Escolha uma opção: ")

	if opcao == "1":
		cadastrar_produto()
	elif opcao == "2":
		calcular_subtotal()
	elif opcao == "3":
		aplicar_desconto()
	elif opcao == "4":
		calcular_pagamento()
	elif opcao == "5":
		exibir_resumo()
	elif opcao == "0":
		sair()
		break
	else:
		print("Opção inválida. Tente novamente.")
