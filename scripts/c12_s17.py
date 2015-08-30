from Bio.PDB import *

parser = PDBParser()
estrutura = parser.get_structure('BGA', '1BGA.pdb')

# Resultado sera gravado num arquivo tabular 
w = open("matriz_distancia.txt","w")

# Preenchendo a primeira linha
for residuo in estrutura[0]['A']:
	if is_aa(residuo):
		rid = residuo.id[1]
		rname = Polypeptide.three_to_one(residuo.resname)
		rnameid = "%s%s" %(rid,rname)
		w.write("\t")
		w.write(rnameid)
		
w.write("\n")


# Preenchendo a matriz
# Para comparacao todos contra todos eh necessario dois lacos
for residuo_C1 in estrutura[0]['A']:
	if is_aa(residuo_C1):

		# Gravamos a primeira coluna
		rid = residuo_C1.id[1]
		rname = Polypeptide.three_to_one(residuo_C1.resname)
		rnameid = "%s%s" %(rid,rname)
		w.write(rnameid)
		w.write("\t")

		# Segundo laco 
		for residuo_C2 in estrutura[0]['A']:
			if is_aa(residuo_C2):
				
				# id e carbono alfa
				rid1 = residuo_C1.id[1]
				rid2 = residuo_C2.id[1]

				ca1 = estrutura[0]['A'][rid1]['CA']
				ca2 = estrutura[0]['A'][rid2]['CA']

				# calculando distancias entre CA
				distancia = ca1 - ca2

				# imprimindo resultados
				w.write(str(distancia))
				w.write("\t")

		w.write("\n")

w.close()