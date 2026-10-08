"""Proposta
Crie uma função recursiva chamada contar_alunos() que receba a quantidade de
alunos e apresente a numeração de 1 até o valor informado.
Teste
contar_alunos(5)
Resultado esperado
Aluno 1
Aluno 2
Aluno 3
Aluno 4
Aluno 5"""

n1 = int(input("digite a quantidade de alunos "))
n = 1
def contarAlunos (n):
    if n > n1:
        print(f"o total de alunos é:{contador}")
    else:
        print(n)
        contarAlunos( n + 1 )
contador=n1
contarAlunos(n)