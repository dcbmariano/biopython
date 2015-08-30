from Bio.PDB import *

parser = PDBParser()

estrutura = parser.get_structure('BGA', '1BGA.pdb')

residuo_100_A = estrutura[0]['A'][100]['CA']
residuo_101_A = estrutura[0]['A'][101]['CA']

distancia = residuo_100_A - residuo_101_A

print distancia
# 3.79421
