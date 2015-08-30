from reportlab.lib import colors
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

# Recebendo o arquivo
arquivo = SeqIO.read("NC_017108.gbk", "genbank")

# Configuracoes basicas
gd_diagram = GenomeDiagram.Diagram("Marcadores")
gd_track_for_features = gd_diagram.new_track(1, name="Anotacoes")
gd_feature_set = gd_track_for_features.new_set()

# Imprime as features de maneira intercalada
for feature in arquivo.features:

	if feature.type == "rRNA":
		color = colors.blue
		gd_feature_set.add_feature(feature, color=color, label=True)

	elif feature.type == "tRNA":
		color = colors.green
		feature.qualifiers['locus_tag'] = feature.qualifiers['product']
		gd_feature_set.add_feature(feature, color=color, label=True)

	elif feature.type == "gene":

		if len(gd_feature_set) % 2 == 0:
			color = colors.HexColor('#BBBBBB')
		else:
			color = colors.HexColor('#DDDDDD')
		
		gd_feature_set.add_feature(feature, color=color, label=False)

	else:
		continue

# Desenhando
gd_diagram.draw(format="circular", circular=True, pagesize=(20*cm,20*cm),start=0, end=len(arquivo), circle_core=0.7)

# Salvand em 2 formatos: PDF e PNG
gd_diagram.write("completo.pdf", "PDF")
gd_diagram.write("completo.png", "PNG")
