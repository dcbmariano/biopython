import sys

if sys.argc > 1:
	arquivo = sys.argv[1]
else:
	print "Sintaxe 'python meu_programa.py [arquivo]’"
	sys.exit()

if arquivo == "-h" or arquivo == '--help':
	print "Sintaxe 'python meu_programa.py [arquivo]’"
	sys.exit()