from Bio.Seq import Seq

seq1 = Seq("AACCGGTT")
seq2 = Seq("AACCGGTT")
seq3 = Seq("TTCCAAGG")

if str(seq1) == str(seq2):
	print "seq1 igual a seq2"

else:
	print "seq1 diferente de seq2"

if str(seq1) == str(seq3):
	print "seq1 igual de seq3"

else:
	print "seq1 diferente de seq3"