from Bio.Blast import NCBIWWW
from Bio import SeqIO

arquivo = SeqIO.read("exemplo.fasta", format="fasta")

print "Iniciando busca no NCBIWWW..."

resultado = NCBIWWW.qblast("blastn", "nt", arquivo.seq, format_type="Text")

print resultado.read()

print "Busca concluida."