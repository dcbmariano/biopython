from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

rna = Seq("AUGGCCAUUCGCAAGGGUGCCCGAUAG", IUPAC.unambiguous_rna)

proteina_rna = rna.translate()

print proteina_rna
# MAIRKGAR*