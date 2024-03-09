# teste.txt

nome_ficheiro = "teste.txt"

# escrever o ficheiro
#ficheiro = open(nome_ficheiro , "w")
#ficheiro.write("Hello ...")
#ficheiro.close()

nome = input("Insira o seu nome: ")
nif = input ("Insira o seu nif: ")
telemovel = ("Insira o seu telemovel: ")

# escrever o ficheiro, sem overwrite
ficheiro = open(nome_ficheiro , "a")
ficheiro.write(f"Nome: {nome} | Nif:{nif} | Telemovel:{telemovel}")
#ficheiro.write("Nome:José Afonso | nif : 349883076 | Telemovel: 969091111\n")
#ficheiro.write("Nome:Mario Afonso | nif : 349883076 | Telemovel: 969091234\n")
#ficheiro.write("Nome:Carlos Afonso | nif : 349883076 | Telemovel: 969091432\n")
#ficheiro.close()


# lêr o ficheiro
ficheiro = open(nome_ficheiro, "r")
conteude = ficheiro.read()
print(conteude)
ficheiro.close