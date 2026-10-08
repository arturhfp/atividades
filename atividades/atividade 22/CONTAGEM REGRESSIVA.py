"""Proposta
Crie uma função recursiva chamada contagem_regressiva() que receba um
número e mostre os valores em ordem decrescente.
Teste
contagem_regressiva(5)
Resultado esperado
5
4

3
2
1"""

def contagem (n):
    if n <= 0:
        print ("que comece a corrida")
    else:
        print(n)
        contagem(n - 1)

contagem(10)    
