from Bio.Blast.Applications import *

comando_blastn = NcbiblastnCommandline(query="example.fasta", subject="example2.fasta", outfmt="'6 qlen qstart qend slen sstart send positive gaps mismatch pident'", out="out.txt")
print comando_blastn

# Executando
stdout, stderr = comando_blastn()

# Abrindo resultado
blast_result = open("out.txt","r")

linhas = blast_result.read()
print linhas