# Exibindo a sequencia reverso complementar com Biopython

from Bio.Seq import Seq
minha_sequencia = Seq("AGTACACTGGT")

print minha_sequencia.reverse_complement()
# ACCAGTGTACT