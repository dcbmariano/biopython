def salvaMapa(mapa, nomeArquivo = 'temporario.txt'):
    ''' O dicionário mapa será salvo no arquivo temporario.txt '''
    arq = open(nomeArquivo,'w')
    for k in mapa.keys():
        linha = 'Coluna: ' + str(k) + ' Valor: ' + str(mapa[k])
        arq.write(linha + '\n')
    arq.close()
    return None

mp = {'A': 'ALA', 'R': 'ARG', 'N':'ASN', 'D':'ASP', 'C':'CYS'}
salvaMapa(mp,'aminoacidos.txt')
