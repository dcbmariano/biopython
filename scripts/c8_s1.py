class Entity(object):
    """
    Classe que contém as características comuns às classes Structure, Model, Chain and Residue.
    """
    def __init__(self, id):
        self.id=id
        self.full_id=None
        self.parent=None
        self.child_list=[]
        self.child_dict={}
        # Dicionário que mantém as propriedades adicionais
        self.xtra={}

    # Métodos especiais

    def __len__(self):
        "Retorna o número de filhos"
        return len(self.child_list)

    def __getitem__(self, id):
        "Retorna o filho correspondente ao id passado."
        return self.child_dict[id]

    def has_id(self, id):
        """Retorna verdadeiro(True) se existir um filho com o id passa-do."""
        return (id in self.child_dict)

    def get_level(self):
        """Retorna o nível na hierarquia.
        A - atom
        R - residue
        C - chain
        M - model
        S - structure
        """
        return self.level

class Chain(Entity):
    def __init__(self, id):
        self.level="C"
        Entity.__init__(self, id)

    def get_atoms(self):
        for r in self:
            for a in r:
                yield a
