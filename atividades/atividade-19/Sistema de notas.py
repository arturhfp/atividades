print("===================================================")
print("[ SISTEMA ESCOLAR - SECRETARIA ACADÊMICA ]       ")
print("===================================================")
print("||                                               ||")
print("||           INSTITUTO EDUCACIONAL TOKYO         ||")
print("||             [ MATRÍCULAS 2026 ]               ||")
print("||                                               ||")
print("||   STATUS: VALIDAÇÃO DE DADOS DE ALUNOS        ||")
print("===================================================")


alunos = []
aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(5):
    print(f"\n[ ALUNO {i + 1} ]")
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota1 = float(input("Digite a primeira nota do aluno: "))
    
    
    aluno = {
        "nome": nome,
        "idade": idade,
        "nota1": nota1,
    }
    alunos.append(aluno)

    if aluno["nota1"] >= 7:
        print("Status: Aprovado")
        aprovados += 1
    elif aluno["nota1"] >= 5:
        print("Status: Recuperação")
        recuperacao += 1
    else:
        print("Status: Reprovado")
        reprovados += 1

print("\n=== Resultado final ===")
print(f"Aprovados: {aprovados}")
print(f"Em recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
