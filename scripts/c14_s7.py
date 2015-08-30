from Bio import SeqIO
from Bio.SeqIO.QualityIO import PairedFastaQualIterator

# FASTQ > FASTA
SeqIO.convert("SRR020192.fastq", "fastq", "SRR020192.fasta", "fasta")

# FASTQ > QUAL
SeqIO.convert("SRR020192.fastq", "fastq", "SRR020192.qual", "qual")

# FASTQ + QUAL > FASTQ
fastq2 = open("novo_fastq.fastq", "w") 
rec = PairedFastaQualIterator(open("SRR020192.fasta"), open("SRR020192.qual"))
i = SeqIO.write(rec, fastq2, "fastq")
fastq2.close()

print "Foram convertidas %i sequencias FASTA + QUAL em formato FASTQ" % i