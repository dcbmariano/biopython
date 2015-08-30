from Bio.PDB import *
parser = PDBParser()
estrutura = parser.get_structure('BGA', '1BGA.pdb')
cabecalho = parser.get_header()

# Metodo de determinacao da estrutura
metodo = estrutura.header['structure_method']

# Resolucao
resolucao = estrutura.header['resolution']

print "Metodo: ", metodo
print "Resolucao: ", resolucao

# Metodo:  x-ray diffraction
# Resolucao:  2.4
