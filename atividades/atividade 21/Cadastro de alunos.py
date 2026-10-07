"""Uma escola precisa desenvolver uma pequena funcionalidade para armazenar os
nomes dos alunos de uma turma.
Os nomes precisam ficar armazenados para que o sistema possa apresentar
todos os alunos cadastrados e também acessar alunos de posições específicas.
O sistema deverá inicialmente possuir cinco alunos. Depois, um novo aluno
deverá ser adicionado.
Estrutura que deve ser utilizada
Lista
A lista é adequada porque os alunos precisam ser armazenados em uma
sequência e podem ser acessados por suas posições.
O que desenvolver
1. Criar uma lista com cinco nomes.
2. Exibir todos os alunos.
3. Exibir o primeiro aluno.
4. Exibir o último aluno.
5. Adicionar um novo aluno.
6. Exibir a lista atualizada.
Resultado esperado
Alunos cadastrados:
Ana
Carlos
Mariana
Pedro
João

Primeiro aluno: Ana
Último aluno: João

Lista atualizada:

Ana
Carlos
Mariana
Pedro
João
Lucas"""

alunos = ["Andrei", "Artur", "Caio", "Vitor", "Gabriel"]

print("Alunos cadastrados:")
for aluno in alunos:
    print(aluno)

print(f"\nPrimeiro aluno: {alunos[0]}")
print(f"Último aluno: {alunos[-1]}")

alunos.append("Joao")

print("\nLista atualizada:\n")
for aluno in alunos:
    print(aluno)
                            
