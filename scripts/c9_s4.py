from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

dna = Seq("ATGGCCATTCGCAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
print "DNA: "+dna
# DNA: ATGGCCATTCGCAAGGGTGCCCGATAG

rna = dna.transcribe()
print "RNA: "+rna
#RNA: AUGGCCAUUCGCAAGGGUGCCCGAUAG

dna2 = rna.back_transcribe()
print "DNA: "+dna2
#DNA: ATGGCCATTCGCAAGGGTGCCCGATAG