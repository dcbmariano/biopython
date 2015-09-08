def imprimeFormatado(*val,**kvals):
    print val
    print kvals

imprimeFormatado('Autores',4, ano = 2015, inicio = ”janeiro”, fim = ”dezembro”)

# ('Autores',4)
# {'ano': 2015, 'inicio':'janeiro', 'fim' :'dezembro'}
