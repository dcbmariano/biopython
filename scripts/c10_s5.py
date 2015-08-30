from Bio import SeqIO
for seq_record in SeqIO.parse("NC_009934.gbk", "genbank"):

    # imprime o cabecalho
    print seq_record.id

    # imprime a sequencia
    print seq_record.seq

    # imprime o tamanho da sequencia
    print len(seq_record)