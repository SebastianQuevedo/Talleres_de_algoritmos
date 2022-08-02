Algoritmo ejercicio_15
		Escribir "ingrese el numero de dos cifras"
		leer a
		b <- a
		Repetir
			b<-b-1
		Hasta Que b%2=0 y b%5=0
		c <- a-b
		d <- (a-c)/10
		Escribir "el resultado es "  c d
	
FinAlgoritmo
