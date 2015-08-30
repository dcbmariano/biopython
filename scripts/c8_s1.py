class Pessoa():

    def __init__(self, nm, idd, sx):
        '''
        Metodo inicializador da classe.
        '''
        self.nome = nm
        self.idade = idd
        self.sexo = sx

    def faz_aniversario(self):
        self.idade += 1

m = Pessoa("Maria", 20, "Feminino")
j = Pessoa("Jose", 15, "Masculino")
print j.idade
# imprime 15
j.faz_aniversario()
print j.idade
#imprime 16