Algoritmo Ejercicio_3
	Escribir "ingrese el largo del rectangulo"
	Leer a
	escribir "ingrese la altura del rectngulo"
	leer b
	Escribir "que quiere obtener"
	escribir "1. area "
	escribir "2. perimetro "
	leer c
	Segun c Hacer
		1:
			d <- a*b
			escribir "el area es " d
		2:
			d <- (a*2)+(b*2)
			escribir "el perimetro es " d
		De Otro Modo:
			Escribir "la opcion no es valida"
	Fin Segun
	
FinAlgoritmo
