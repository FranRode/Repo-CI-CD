def buscar_minimo(lista):
	minimo = lista[0]
	for i in lista:
		if i < minimo:
			minimo = i
	return minimo