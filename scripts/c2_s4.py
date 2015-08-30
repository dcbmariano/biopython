idade = int(raw_input("Digite usa idade: "))

if ((idade >= 0) and (idade < 16)):
	print "Voce nao pode votar!"

elif (((idade >= 16) and (idade < 18)) or (idade >= 70)):
	print "Voto opcional!"
elif ((idade >= 18) and (idade < 70)):
	print "Voto obrigatorio!"
else:
	print "Idade invalida!"