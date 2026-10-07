"""Uma loja precisa apresentar os produtos disponíveis em seu sistema.
Os produtos estão armazenados em uma estrutura e o sistema deverá percorrer
todos os elementos para apresentá-los na tela.
Estrutura que deve ser utilizada
Lista
A lista é adequada para armazenar os diversos produtos e permitir que eles sejam
percorridos.
O que desenvolver
1. Criar uma lista com cinco produtos.
2. Utilizar um for para percorrer a lista.
3. Apresentar cada produto na tela.
Resultado esperado
Produtos disponíveis:

Teclado
Mouse
Monitor
Impressora
Webcam"""


print("===================================================")
print("[ SISTEMA DE CONTROLE DE ESTOQUE - LOGÍSTICA ]    ")
print("===================================================")
print("||                                               ||")
print("||           W. H. S. - WAREHOUSE HUB            ||")
print("||             [ INVENTÁRIO ATIVO ]              ||")
print("||                                               ||")
print("||   STATUS: ENTRADA E SAÍDA DE PRODUTOS OK      ||")
print("===================================================")

print("\nProdutos disponíveis:\n")
produtos = ["ps5", "lenovo LOQ", "poco x8 pro", "sandevistan", "teclado mecânico"]
for produto in produtos:
    print(produto)
    