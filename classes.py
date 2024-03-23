class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
        print(nome)

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
vaca=Animal("vaca")
vaca.set_nome("vaquinha")
print(vaca.get_nome())