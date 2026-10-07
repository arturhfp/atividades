"""Um sistema escolar precisa armazenar as notas de cinco alunos.
Depois de armazenar as notas, o sistema deverá percorrer os valores e calcular a
soma e a média da turma.
Estrutura que deve ser utilizada
Lista
A lista permite armazenar diversas notas em uma única estrutura e percorrer
todos os valores.
O que desenvolver
1. Criar uma lista com cinco notas.
2. Percorrer as notas utilizando for.
3. Calcular a soma.
4. Calcular a média.
5. Apresentar os resultados.
Resultado esperado
Considerando as notas:
7
8
6
9
10
O sistema deverá apresentar algo semelhante a:
Notas:
7
8
6
9
10

Soma: 40

Média: 8.0"""


print("===================================================")
print("[ SISTEMA ESCOLAR - SECRETARIA ACADÊMICA ]       ")
print("===================================================")
print("||                                               ||")
print("||           INSTITUTO EDUCACIONAL TOKYO         ||")
print("||                                               ||")
print("||   STATUS: VALIDAÇÃO DE DADOS DE ALUNOS        ||")
print("===================================================")

soma = 0 

print("\nNotas:\n")
notas = [9, 5, 7, 10, 1]
for nota in notas:
    print(nota)
    soma += nota
    media = soma / len(notas)

print(f"\nSoma: {soma}")
print(f"Média: {media}")
