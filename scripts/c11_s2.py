from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO

arquivo = SeqIO.read("exemplo.fasta", format="fasta")

print "Iniciando busca no NCBIWWW..." 

resultado = NCBIWWW.qblast("blastn", "nt", arquivo.seq, format_type="XML")

print "Busca concluida. Salvando resultados..."

saida = open("blast_resultado.xml", "w")
saida.write(resultado.read())
saida.close() 


# Lendo arquivos XML

arquivo_xml = open("blast_resultado.xml","r")
dados = NCBIXML.parse(arquivo_xml)
item = next(dados)

i = 1

for a in item.alignments:
	for hsp in a.hsps:
		print 'Alinhamento',i
		print 'Sequencia: '+a.title
		print 'Tamanho: ',a.length
		print 'Score: ',hsp.score
		print 'Gaps: ',hsp.gaps
		print hsp.query 
		print hsp.match
		print hsp.sbjct
		print "\n"
		i+=1

print "Executado com sucesso."