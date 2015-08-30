'''
Titulo: calculadora.py
Funcao: efetua somas, subtracoes, divisoes e multiplicacoes
'''

print "CALCULADORA"

sair = False

while sair == False:

	num1 = input("Digite o primeiro numero: ")

	operador = input("Digite a operacao desejada (1 para soma, 2 para subracao, 3 para divisao e 4 para multiplicacao): ")

	num2 = input("Digite o segundo numero: ")

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

	opcao = int(input("Digite 1 para encerrar a calculadora ou 2 para realizar outra operacao"))

	if opcao == 1:
		sair = True