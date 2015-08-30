from Bio.Seq import Seq

seq1 = Seq('AAA')
seq2 = Seq('TTT')
seq3 = Seq('CCC')
seq4 = Seq('GGG')

seq_final = seq1 + seq2 + seq3 + seq4

print seq_final
# AAATTTCCCGGG