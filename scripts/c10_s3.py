from Bio import SeqIO
for i in SeqIO.parse("arquivo.fasta", "fasta"):

    # imprime o cabecalho
    print i.id

    # imprime a sequencia
    print i.seq

    # imprime o tamanho da sequencia
    print len(i)