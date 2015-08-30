import sys

nome_arquivo = sys.argv[1]
arquivo = open(nome_arquivo)
linhas = arquivo.readlines()
for linha in linhas:
	print(linha)