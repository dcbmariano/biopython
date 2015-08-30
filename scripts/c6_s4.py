arq = open("meu_arquivo2.txt","w+")
linhasParaOArquivo = ["linha 1","linha 2","linha 3","linha 4","linha 5"]
for lnh in linhasParaOArquivo:
    arq.write(lnh)
    arq.write("\n")

arq.close()