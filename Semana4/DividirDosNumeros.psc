Algoritmo DividirDosNumeros
	Definir num1, num2, resultado Como Real
	Escribir "Ingrese el dividendo:"
	Leer num1
	Escribir "Ingrese el divisor:"
	Leer num2
	Si num2 <> 0 Entonces 
		resultado = num1 / num2 
		Escribir "El resultado es: ", resultado
		Sino
			Escribir "Error: No se puede dividir entre cero."
			Finsi
FinAlgoritmo
