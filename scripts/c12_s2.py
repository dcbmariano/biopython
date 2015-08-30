# Importando Bio.PDB
from Bio.PDB import *

# Criando um objeto PDBParser
parser = PDBParser()

# Declarando a estrutura
estrutura = parser.get_structure('BGA', '1BGA.pdb')