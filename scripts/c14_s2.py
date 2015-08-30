# Calculo de N50

# Declaracoes iniciais
from Bio import SeqIO
import sys

sum_tamanhos = 0
sumcontig = 0
todos_tamanhos = list()

# Recebemos o arquivo como parametro
arquivo = sys.argv[1]

# Laco le todos os tamanhos 
for i in SeqIO.parse(arquivo,"fasta"):
	tam_contig = len(i.seq)
	todos_tamanhos.append(tam_contig)
	sumcontig = sumcontig + tam_contig


# Ordenamos todos os tamanhos
todos_tamanhos.sort()

# Calcula metade da soma das sequencias
v50 = sumcontig/2

# Laco para detectar N50
for tam in todos_tamanhos:
	sum_tamanhos = sum_tamanhos + tam
	if sum_tamanhos > v50:
		n50 = tam
		break

print "N50: ",n50