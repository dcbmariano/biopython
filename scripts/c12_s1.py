from Bio.PDB import *

# Fazendo download da estrutura 1BGA
pdb = PDBList()
pdb.retrieve_pdb_file('1BGA')