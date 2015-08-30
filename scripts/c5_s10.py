aminoacidos = {'alanina': ['ALA', 'A'], 'cisteina': ['CYS','C']}

# Mais amino
aminoacidos['histidina'] = ['HIS', 'H']

for um, tres in aminoacidos.items():
	print um, '=>', tres

'''
cisteina => ['CYS', 'C']
histidina => ['HIS', 'H']
alanina => ['ALA', 'A']
'''