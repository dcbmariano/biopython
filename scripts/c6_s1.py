arq = open("meu_arquivo.txt")
linhas = arq.readlines()
for linha in linhas:
    print(linha)