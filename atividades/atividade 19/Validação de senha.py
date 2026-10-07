'''Um sistema possui uma senha de acesso.
O usuário deverá informar a senha até acertar.
Enquanto a senha estiver incorreta, o programa deverá solicitar uma nova
tentativa.
Utilize while para implementar essa situação.
Quando a senha estiver correta, apresente uma mensagem informando que o
acesso foi liberado.'''

print("===================================================")
print("[ EMERGENCY - NERV SECURE TERMINAL ]             ")
print("===================================================")
print("||                                               ||")
print("||                A T . F I E L D                ||")
print("||             [ SYNCHRONIZING... ]              ||")
print("||                                               ||")
print("||   STATUS: EVA-01 LCL COMPARTMENT SECURED      ||")
print("===================================================")

senhaGendo = 123456
senhaGuts = 1234
senhaShinji = 6172
senha = ""

while True :

    print("===================================================")    
    senha = int(input("Digite a senha de acesso: "))

    if senha == senhaGendo:
        print("Acesso liberado para Gendo Ikari.")
        break
    elif senha == senhaGuts:
        print("Acesso liberado para Guts.")
        break
    elif senha == senhaShinji:
        print("Acesso liberado para Shinji Ikari.")
        break
    else:
        print("Senha incorreta. Tente novamente.")

print("===================================================")
print("sessão encerrada.   ")