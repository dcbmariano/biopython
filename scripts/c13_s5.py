from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

# Recebendo o arquivo
arquivo = SeqIO.read("NC_009934.gbk", "genbank")

# Configuracoes basicas
gd_diagram = GenomeDiagram.Diagram("Plasmideo")
gd_track_for_features = gd_diagram.new_track(1, name="Anotacoes")
gd_feature_set = gd_track_for_features.new_set()

# Imprime as features de maneira intercalada
for feature in arquivo.features:
    if feature.type != "gene":
        # Despreza a feature que nao sao genes
        continue
    if len(gd_feature_set) % 2 == 0:
        color = colors.HexColor('#79B134')
    else:
        color = colors.HexColor('#8DE91D')
    gd_feature_set.add_feature(feature, color=color, label=True)

# Desenhando
gd_diagram.draw(format="circular", circular=True, pagesize=(20*cm,20*cm),start=0, end=len(arquivo), circle_core=0.7)

# Salvand em 2 formatos: PDF e PNG
gd_diagram.write("plasmideo.pdf", "PDF")
gd_diagram.write("plasmideo.png", "PNG")