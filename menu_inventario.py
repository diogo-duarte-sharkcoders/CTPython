def menu_principal():
    while True:
        print("1-Registar cliente\n2-Criar inventário\n3-Apagar biblioteca")
        op = int(input("Insira uma opcão\n>"))
        if op == 1:
            input("Escreva o nome da biblioteca\n>")
        elif op == 2:
            input("Escreva um nome para dar para a biblioteca\n>")
        elif op == 3:
            print("Tem acerteza?")
            Apagar = input("y ou n")
        else:
            print("Opcão inválida")


           

            

     
