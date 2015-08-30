from Bio import SeqIO
from Bio.SeqUtils import GC
import pylab

for i in SeqIO.parse("NC_017108.gbk", "genbank"):
	gc = GC(i.seq)

at = 100-gc

pylab.pie([gc,at])
pylab.title("Conteudo GC:")
pylab.xlabel("GC: %0.1f porcento\nAT: %0.1f porcento" % (gc,at))
pylab.show()