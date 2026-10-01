print("===================================================")
print("[ EMERGENCY - NERV SECURE TERMINAL ]             ")
print("===================================================")
print("||                                               ||")
print("||                A T . F I E L D                ||")
print("||             [ SYNCHRONIZING... ]              ||")
print("||                                               ||")
print("||   STATUS: EVA-01 LCL COMPARTMENT SECURED      ||")
print("===================================================")


perfis = [
    {"usuario1": "guts Miura", "senha1": "1234"},
    {"usuario2": "shinji Ikari", "senha2": "5678"},
    {"usuario3": "gendo Ikari", "senha3": "9012"}
]

tentativas = 0
while True:
    if tentativas == 3:
        print("Você excedeu o número máximo de tentativas. Acesso bloqueado.")
        exit()
        
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if perfis[0]["usuario1"] == usuario and perfis[0]["senha1"] == senha:
            print(f"Acesso liberado para {perfis[0]['usuario1']}.")
            exit()
    elif perfis[1]["usuario2"] == usuario and perfis[1]["senha2"] == senha:
            print(f"Acesso liberado para {perfis[1]['usuario2']}.")
            exit()
    elif perfis[2]["usuario3"] == usuario and perfis[2]["senha3"] == senha:
            print(f"Acesso liberado para {perfis[2]['usuario3']}.")
            exit()
    
    else:
            tentativas += 1
            print("Usuário ou senha incorretos. Tente novamente.")