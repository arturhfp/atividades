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

print ("Bem-vindo ao sistema de controle de estoque da W.H.S.")

while True:
    print("\n1 - cadastrar produto")
    print("2 - consultar produto")
    print("3 - informações do produto")
    print("4 - quantidade de produto")
    opcao = input("escolha uma opção")
    if opcao == 1 :
        codigoProduto = float(input("digite o codigo do produto:"))
        nomeProduto = input("digite o nome do produto:")
        categoria = input("digite a categoria do produto:")
        quantidade = float(input("digite a quantidade disponivel:"))
        preco = float(input("digite o preco do produto:"))

