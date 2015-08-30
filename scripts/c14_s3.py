from Bio import SeqIO

# Declarando variavel contadora i
i = 0

# Contando registros
for seq in SeqIO.parse("SRR020192.fastq", "fastq"):
    i += 1

print "Foram detectadas %i leituras." % i

# Foram detectadas 41892 leituras.