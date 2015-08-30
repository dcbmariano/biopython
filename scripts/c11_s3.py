from Bio.Blast.Applications import *

comando_blastn = NcbiblastnCommandline(query="exemplo.fasta", subject="exemplo2.fasta", outfmt=0, out="out.txt")
print comando_blastn

# Executando
stdout, stderr = comando_blastn()

# Abrindo resultado
blast_result = open("out.txt","r")

linhas = blast_result.read()
print linhas