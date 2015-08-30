from Bio import SeqIO

# Lendo as sequencias
sequencias = list(SeqIO.parse("NC_017108.ffn","fasta"))

# Realizando o ordenamento
sequencias.sort(cmp=lambda x,y: cmp(len(x),len(y)))

# Gravando o resultado 
if SeqIO.write(sequencias, "sequencias_ordenadas.fasta", "fasta"):
	print "Sequencias ordenadas com sucesso."
else:
	print "Um erro ocorreu."