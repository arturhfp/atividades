print ("Sistema de resultado escolar")

nomeAluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
    print("Erro: as notas devem estar entre 0 e 10.")
    exit()
percentualFrequencia = float(input("Digite o percentual de frequência do aluno: "))
if percentualFrequencia < 0 or percentualFrequencia > 100:
    print("Erro: o percentual de frequência deve estar entre 0 e 100.")
    exit()                
media = (nota1 + nota2 + nota3) / 3        
if media >= 7 and percentualFrequencia >= 75:
    resultadoFinal = "Aprovado"
elif media >= 7 and percentualFrequencia < 75:
    resultadoFinal = "Reprovado por falta"     
elif media >= 5 and media < 7 and percentualFrequencia >= 75:
    resultadoFinal = "Recuperação"
elif media <= 5 and percentualFrequencia >= 75:
    resultadoFinal = "Reprovado por nota"
elif media < 5 and percentualFrequencia < 75:
    resultadoFinal = "Reprovado por nota e falta"
else:
    resultadoFinal = "Reprovado por falta"    
print(f"Aluno: {nomeAluno}")
print(f"Média: {media}")
print(f"Percentual de Frequência: {percentualFrequencia}")
print(f"Resultado Final: {resultadoFinal}")