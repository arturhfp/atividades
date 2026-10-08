"""Proposta
Crie uma função recursiva chamada mostrar_mensagem() que receba uma
mensagem e a quantidade de vezes que ela deverá ser apresentada.
Teste
mostrar_mensagem("Atenção!", 3)
Resultado esperado
Atenção!
Atenção!
Atenção!"""

from time import sleep


alerta = input("digite a mensagem de alerta: ")
n = int(input("quantas vezes deseja replicar essa mensagem? "))

def mostrar_mensagem(alerta,n):
    if n > 0:
        sleep(1)
        print(alerta)
        n -= 1
        mostrar_mensagem(alerta,n)
    else: 

        print("fim")
        exit()
mostrar_mensagem(alerta,n)