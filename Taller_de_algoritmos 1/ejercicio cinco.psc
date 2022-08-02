Algoritmo ejercicio_5
	Escribir "elija la operacion que quiere ejecutar"
	escribir "1. suma"
	escribir "2. resta"
	escribir "3. multiplicacion"
	escribir "4. division"
	escribir "5. potencia"
	escribir "6. todas"
	escribir "recuerde que debe escribir el numero de la lista"
	Leer N
	Segun N Hacer
		1:
			Escribir "elige el numero 1"
			Leer a
			Escribir "elige el numero 2"
			Leer b
			c <-a+b
			escribir "su resultado es " c
			
		2:
			Escribir "elige el numero 1"
			Leer a
			Escribir "elige el numero 2"
			Leer b
			c <-a-b
			escribir "su resultado es " c
		3:
			Escribir "elige el numero 1"
			Leer a
			Escribir "elige el numero 2"
			Leer b
			c <-a*b
			escribir "su resultado es " c
		4:
			Escribir "elige el numero 1"
			Leer a
			Escribir "elige el numero 2"
			Leer b
			c <-a/b
			escribir "su resultado es " c
		5:
			Escribir "elige el numero 1"
			Leer a
			Escribir "elige el numero 2"
			Leer b
			c <-a^b
			escribir "su resultado es " c
		6: 
			Escribir "elige el numero 1"
			Leer a
			Escribir "elige el numero 2"
			Leer b
			c <-a+b
			d <-a-b
			e <-a*b
			f <-a/b
			g <-a^b
			
			escribir "el resultado de la suma es " c
			escribir "el resultado de la resta es " d
			escribir "el resultado de la multiplicacion es " e
			escribir "el resultado de la division es " f
			escribir "el resultado de la potencia es " g
		De Otro Modo:
			escribir "la opcion que eligio no esta disponible"
	Fin Segun
FinAlgoritmo
