from Bio import SeqIO
import pylab

arquivo = open("SRR020192.fastq")
parse = list(SeqIO.parse(arquivo,"fastq"))
tam_seq = []
max_seqs = []
min_seqs = []
media = []

for i in parse:
	tam_seq.append(len(i.seq))

max_seq = max(tam_seq)
min_seq = min(tam_seq)
total_seq = len(parse)

for j in range(max_seq):
	aux = 0
	mas = 0
	mis = max_seq
	for i in parse:
		if(len(i.seq) < max_seq):
			i.letter_annotations["phred_quality"].append(0)
		aux = aux + i.letter_annotations["phred_quality"][j]

		if mas < i.letter_annotations["phred_quality"][j]:
			mas = i.letter_annotations["phred_quality"][j]

		if mis > i.letter_annotations["phred_quality"][j]:
			mis = i.letter_annotations["phred_quality"][j]

	media.append(int(aux/total_seq))
	max_seqs.append(mas)
	min_seqs.append(mis)

pylab.plot(media,'-k',label="Media", linewidth=2)
pylab.plot(max_seqs,'-g',label="Max")
pylab.plot(min_seqs,'-r',label="Min")
pylab.grid(color='gray', linestyle=':', linewidth=1)
pylab.legend()
pylab.ylim(0,45)
pylab.ylabel("PHRED")
pylab.xlabel("Leitura (pb)")
pylab.savefig("grafico_qualidade.png")

pylab.show()