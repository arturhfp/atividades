print("situaçao do aluno")

def verificar_situacao(nota):
    if nota >= 7:
     return "aluno aprovado"
    elif nota > 5:
     return "aluno em recuperação"
    elif nota < 5:
     return "aluno reprovado"


nota = float(input("digite a nota do aluno: "))
nomeALuno = input("digite o nome do aluno: ")

situacao = verificar_situacao(nota)

print(f"o aluno {nomeALuno} está {situacao}")