"""Um sistema possui uma funcionalidade para desfazer as últimas ações realizadas
pelo usuário.
Por exemplo, o usuário realizou cinco ações. Ao selecionar a opção "Desfazer", a
última ação realizada deverá ser desfeita primeiro.
Estrutura que deve ser utilizada

Pilha
A pilha é adequada porque a última ação realizada deve ser a primeira a ser
desfeita.
O que desenvolver
Adicione as seguintes ações:
Digitou o nome
Alterou o endereço
Adicionou um produto
Alterou o telefone
Excluiu um produto
Depois, utilize uma pilha para desfazer as ações.
Resultado esperado
Desfazendo: Excluiu um produto
Desfazendo: Alterou o telefone
Desfazendo: Adicionou um produto
Desfazendo: Alterou o endereço
Desfazendo: Digitou o nome
Observe que a ordem de saída é inversa da ordem de entrada."""

acoes = ["Digitou o nome", "Alterou o endereço", "Adicionou um produto", "Alterou o telefone", "Excluiu um produto"]

print("\n===================================================")
print("        [ SISTEMA - DESFAZER AÇÕES ]               ")    
print("===================================================")

while acoes:
    acao_desfeita = acoes.pop()
    print(f"Desfazendo: {acao_desfeita}")