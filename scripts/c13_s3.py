from Bio import SeqIO
from Bio.SeqUtils import GC
import pylab

# Parte 1 - Abrindo arquivo GBK
for i in SeqIO.parse("NC_017108.gbk", "genbank"):
	seq = str(i.seq)

# Parte 2 - Variaveis importantes
tamanho = len(seq)
fragmentos = int(tamanho / 1000)
gc = []

# Parte 3 - Armazenando conteudo GC
for i in range(fragmentos):
	j = i * 1000
	k = j + 999
	gc_atual = GC(seq[j:k])
	gc.append(gc_atual)
	print i,": ",j,"-",k,"- GC =",gc_atual,"%"

# Parte 4 - Adicionando o ultimo elemento
resto = tamanho % 1000
j = (i+1) * 1000
k = j + resto
gc_ultimo = GC(seq[j:k])
gc.append(gc_ultimo)
print i+1,": ",j,"-",k,"- GC =",gc_ultimo,"%"

# Parte 5 - Imprimindo grafico
pylab.plot(gc)
pylab.title("Conteudo GC\n%i fragmentos de 1000 pb variando de %0.1f%% a %0.1f%%" % (len(gc),min(gc),max(gc)))
pylab.xlabel("Tamanho (Kb)")
pylab.ylabel("GC%")
pylab.show()