# [...] 
i = 1
for residuo in cadeia:
    if residuo.id[0] != ' ':
        cadeia.detach_child(residuo.id)
    else:	
        residue.id = (' ', i, ' ')
        i += 1
# […]