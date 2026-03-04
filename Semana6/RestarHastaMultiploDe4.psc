Algoritmo RestarHastaMultiploDe4
		// Definición de variables
		Definir num, resta Como Entero
		
		Escribir "Ingrese un número inicial:"
		Leer num
		
		// El ciclo "Hacer-Mientras" (Repetir-Hasta Que)
		// Se ejecutará mientras el número NO sea múltiplo de 4
		Repetir
			Escribir "Ingrese la cantidad a restar:"
			Leer resta
			
			num = num - resta
			
			Escribir "El valor actual es: ", num
			
			Si num % 4 == 0 Entonces
				Escribir "¡Éxito! ", num, " es múltiplo de 4."
			Sino
				Escribir num, " no es múltiplo de 4. Continúa restando."
			FinSi
			
		Hasta Que num % 4 == 0
		
		Escribir "Fin del programa. El resultado final es: ", num
FinAlgoritmo

