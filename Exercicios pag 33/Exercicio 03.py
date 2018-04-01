tudoCerto = 0

while tudoCerto != 1:
    usuario = input("Por favor, digite um usuario valido ")
    senha = input("Por favor digite uma senha valida: ")

    if usuario !=senha:
        tudoCerto = 1
    else:
        tudoCerto =0
        print("Usuario e senha iguais, insira dados validos! ")
