print ("media dos alunos")
#definir 
def calcular_media(nota1,nota2,nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

media = calcular_media(nota1,nota2,nota3)

print (f"a media é, {media}")


