from Bio import SeqIO

entrada = open("arquivo1.fasta","r")
saida = open("arquivo2.fasta", "w")

for i in SeqIO.parse(entrada,"fasta"):
	
	# Condicao 1 (> 10 pb) | Condicao 2 (seq[0] == 'C')
	if ( (len(i.seq) > 10) and (i.seq[0] == 'C') ):
		SeqIO.write(i, saida, "fasta")

saida.close()