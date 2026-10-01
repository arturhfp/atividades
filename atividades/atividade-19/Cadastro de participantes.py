##Um sistema precisa cadastrar 5 participantes de uma atividade.
##Utilize um laço for para solicitar o nome de cada participante.

print  ("participantes de uma entrevista")

nomes = []

for i in range (1,6):
    nome =  input(f"escreva o nome do participante {i}: ")
    nomes.append(nome)

i -= 4

for nome in nomes :
    print (f"{i} - {nome}")
    i += 1