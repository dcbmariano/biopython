from Bio.PDB import *

parser = PDBParser()
estrutura = parser.get_structure('BGA', '1BGA.pdb')

for modelo in estrutura:
    print "Modelo: ", modelo.id
    for cadeia in modelo:
        print "\t - Cadeia: ", cadeia.id
        for residuo in cadeia:
            print "\t\t - Residuo: ",residuo.resname,"(",residuo.id[1],")"
            for atomo in residuo:
                print "\t\t\t - Atomo:",atomo.name,"-> Coordenadas: ( X:",atomo.coord[0],"- Y:",atomo.coord[1],"- Z:",atomo.coord[2],")"