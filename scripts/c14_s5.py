from Bio import SeqIO

boas_leituras = (rec for rec in \
              SeqIO.parse("SRR020192.fastq", "fastq") \
              if min(rec.letter_annotations["phred_quality"]) >= 20)

# Contador i
i = SeqIO.write(boas_leituras, "boa_qualidade.fastq", "fastq")

print "Foram salvas %i leituras com qualidade maior ou igual a 20." % i

# Foram salvas 20050 leituras com qualidade maior ou igual a 20.