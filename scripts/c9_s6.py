from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

dna = Seq("ATGGCCATTCGCAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)

proteina_dna = dna.translate()

print proteina_dna
# MAIRKGAR*