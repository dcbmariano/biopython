'''
Titulo: par_ou_impar.py
Funcao: determinar se um numero eh par ou impar
'''

# Recebe um numero digitado pelo usuario
num = input("Digite um numero: ")
resto = num % 2 

# Testa se o numero eh par ou impar
if resto == 0:
	print "O numero digitado eh par."
else:
	print "O numero digitado eh impar."