'''
Titulo: calculadora.py
Funcao: efetua somas, subtracoes, divisoes e multiplicacoes
'''

print "CALCULADORA"

num1 = input("Digite o primeiro numero: ")

operador = input("Digite a operacao desejada (1 para soma, 2 para subracao, 3 para divisao e 4 para multiplicacao): ")

num2 = input("Digite o segundo numero: ")

# Determinando qual o operador foi utilizado
if operador == 1:
	operacao = num1 + num2

elif operador == 2:
	operacao = num1 - num2

elif operador == 3:
	operacao = num1 / num2

elif operador == 4:
	operacao = num1 * num2

else:
	operacao = "Operador invalido. Use: 1, 2, 3 ou 4"

print "Resultado: "

print operacao