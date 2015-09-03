from Bio import SeqIO
from Bio.Graphics import GenomeDiagram
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics.GenomeDiagram import CrossLink
from reportlab.lib import colors
from Bio.Blast.Applications import *

import sys

# Recebendo os dados pela chamada do programa
A = sys.argv[1]
B = sys.argv[2]

A1 = SeqIO.read(A,"genbank")
B1 = SeqIO.read(B,"genbank")


# BLAST
SeqIO.convert(A, "genbank", A+".fasta", "fasta")
SeqIO.convert(B, "genbank", B+".fasta", "fasta")
comando_blastn = NcbiblastnCommandline(query=A+".fasta", subject=B+".fasta", outfmt="'6 qstart qend sstart send pident'",out="blast_"+A+"_"+B+".txt")
stdout, stderr = comando_blastn()
blast = open("blast_"+A+"_"+B+".txt")

# Iniciando a figura
name = A+"_"+B
gd = GenomeDiagram.Diagram(name)

gA = gd.new_track(1,name="A",height=0.5,start=0,end=len(A1))
gA1 = gA.new_set()
gB = gd.new_track(3,name="B",height=0.5,start=0,end=len(B1))
gB1 = gB.new_set()

# Cores CDSs - intercalado
c1 = "#79B134"
c2 = "#8DE91D"

# Colore um quadrado para cada CDS do arquivo A
cont = 1
for i in A1.features:

	if i.type == "CDS":

		if cont % 2 == 1:
			color_atual = c1
		else:
			color_atual = c2
		gA1.add_feature(i, label=False,label_position="start",color=color_atual)

		cont += 1

	if i.type == "rRNA":
		color_atual = colors.blue
		gA1.add_feature(i, label=False,label_position="start",color=color_atual)

# Colore um quadrado para cada CDS do arquivo B
cont = 1
for i in B1.features:

	if i.type == "CDS":
		if cont % 2 == 1:
			color_atual = c1
		else:
			color_atual = c2
		gB1.add_feature(i, label=False,label_position="start",color=color_atual)
		cont += 1

	if i.type == "rRNA":
		color_atual = colors.blue
		gB1.add_feature(i, label=False,label_position="start",color=color_atual)

# Marca na figura os trechos sintenicos
for b in blast:
	qstart = int(b.split("\t")[0])
	qend = int(b.split("\t")[1])
	sstart = int(b.split("\t")[2])
	send = int(b.split("\t")[3])
	identidade = (float(b.split("\t")[4])*0.8)/100

	# Detectando inversoes
	qinv = qend - qstart
	sinv = send - sstart

	if (qinv > 0 and sinv > 0) or (qinv < 0 and sinv < 0):
		cor = colors.Color(1,.341176,.341176,identidade)
	else:
		cor = colors.firebrick
		
	gd.cross_track_links.append(CrossLink((gA, qstart, qend),(gB, sstart, send),color=cor))

gd.draw(format="linear", pagesize=(8*cm,29.7*cm), fragments=1)

gd.write(name + ".pdf", "PDF")