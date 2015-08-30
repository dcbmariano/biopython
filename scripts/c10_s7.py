from Bio import SeqIO

# Recebendo arquivo GBK
exemplo = SeqIO.read("NC_009934.gbk", "genbank")

for i in exemplo.features:
	if i.type == 'CDS':
		print i.qualifiers['product']