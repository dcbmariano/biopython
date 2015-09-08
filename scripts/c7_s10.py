def mediana(*valores):
    tam = len(valores)
    if tam == 0:
        return None
    elif tam%2 == 0:
        ctr  =  tam/2
        return (valores[ctr] + valores[ctr -1] ) / 2 
    else:
        return valores[tam/2] 

mediana(2,5,6,7,9,12,20) 
# retornaria o valor 7

mediana(2,5,6,7,9,12,20,52)
# retornaria o valor 8
