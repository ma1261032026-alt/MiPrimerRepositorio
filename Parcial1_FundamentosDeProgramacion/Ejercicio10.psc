Algoritmo Ejercicio10
	
	Definir num1, num2 Como Real
	
	Escribir "Ingrese el primer numero:"
	
	leer num1
	
	Escribir "Ingrese el segundo numero:"
	
	leer num2
	
	Si num1 = num2 Entonces
		Escribir "Ambos numeros son iguales"
	SiNo
		Si num1 > num2 Entonces
			Escribir "El mayor es:" , num1
			Escribir "El menor es:" , num2
		SiNo
			Escribir "El mayor es:" , num2
			Escribir "El menor es:" num1
		FinSi
	FinSi
	
FinAlgoritmo
