nucleotideos = ["A","T","C","G"]

nucleotideos.extend(["G", "C"])
print nucleotideos
# Sera impresso  ['A', 'T', 'C', 'G', 'G', 'C']

indice = nucleotideos.index("C")
print indice
# Sera impresso  2

nucleotideos.remove("G")
print nucleotideos
# Sera impreso ['A', 'T', 'C', 'G', 'C']

x = nucleotideos.pop(4)
print x
# Sera impresso "C"

print nucleotideos
# Sera impresso ['A', 'T', 'C', 'G']

del nucleotideos[2:4]
print nucleotideos
# Sera impresso ['A', 'T']

if "A" in nucleotideos:
	print "Exite um A em nucleotideos"
# Sera impresso True

print len(nucleotideos)
# Sera impresso 2