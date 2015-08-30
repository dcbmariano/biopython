from Bio import SeqIO
import pylab

handle = open("exemplo.fasta")
record_iterator = SeqIO.parse(handle, "fasta")
rec_one = next(record_iterator)
rec_two = next(record_iterator)
handle.close()

# Definindo tamanho de janela
window = 11
dict_one = {}
dict_two = {}

# Comparacoes
for (seq, section_dict) in [(str(rec_one.seq).upper(), dict_one),
                            (str(rec_two.seq).upper(), dict_two)]:
    for i in range(len(seq)-window):
        section = seq[i:i+window]
        try:
            section_dict[section].append(i)
        except KeyError:
            section_dict[section] = [i]

matches = set(dict_one).intersection(dict_two)
print("%i k-mers identicos" % len(matches))

# Determinando posicoes x e y
x = []
y = []
for section in matches:
    for i in dict_one[section]:
        for j in dict_two[section]:
            x.append(i)
            y.append(j)

pylab.cla() 
pylab.gray()
pylab.scatter(x,y)
pylab.xlim(0, len(rec_one)-window)
pylab.ylim(0, len(rec_two)-window)
pylab.xlabel("%s (tamanho %i pb)" % (rec_one.id, len(rec_one)))
pylab.ylabel("%s (tamanho %i pb)" % (rec_two.id, len(rec_two)))
pylab.title("Grafico de pontos com janela de %i pb\n(sem mismatches)" % window)
pylab.show()