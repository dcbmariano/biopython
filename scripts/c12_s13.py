from Bio.PDB import *

parser = PDBParser()
peptideos = CaPPBuilder()

estrutura = parser.get_structure('BGA', '1BGA.pdb')

# Criando um arquivo FASTA
w = open("1BGA.fasta","w")

for cadeia in estrutura[0]:
	cadeia_atual = cadeia.id

	for seq in peptideos.build_peptides(cadeia): 
		seq_atual = seq.get_sequence()
		tamanho_seq_atual = len(seq_atual)

		seq_fasta = ">Cadeia_%s_tamanho_%d\n%s\n" %(cadeia_atual,tamanho_seq_atual,seq_atual)
		print seq_fasta
		
		w.write(seq_fasta)

w.close()
w.closed