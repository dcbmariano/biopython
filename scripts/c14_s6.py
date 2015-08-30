from Bio import SeqIO

# Detectando sequencias que tem primer

primer_reads = (rec for rec in \
                SeqIO.parse("SRR020192.fastq", "fastq") \
                if rec.seq.startswith("GATGACGGTGT"))
SeqIO.write(primer_reads, "com_primer.fastq", "fastq")


# Detectando sequencias sem primer

trimmed_primer_reads = (rec[11:] for rec in \
                        SeqIO.parse("SRR020192.fastq", "fastq") \
                        if rec.seq.startswith("GATGACGGTGT"))
SeqIO.write(trimmed_primer_reads, "com_primer_cortado.fastq", "fastq")


# Criando um novo FASTQ

def trim_primer(record, primer):
    if record.seq.startswith(primer):
        return record[len(primer):]
    else:
        return record

trimmed_reads = (trim_primer(record, "GATGACGGTGT") for record in \
                 SeqIO.parse("SRR020192.fastq", "fastq"))
SeqIO.write(trimmed_reads, "cortado.fastq", "fastq")


# Unindo os resultados

def trim_primers(records, primer):
	# Remove primers no inicio das leituras
    len_primer = len(primer) 

    for record in records:
        if record.seq.startswith(primer):
            yield record[len_primer:]
        else:
            yield record

original_reads = SeqIO.parse("SRR020192.fastq", "fastq")
trimmed_reads = trim_primers(original_reads, "GATGACGGTGT")
i = SeqIO.write(trimmed_reads, "cortado.fastq", "fastq")

print "Foram salvas %i leituras" % i