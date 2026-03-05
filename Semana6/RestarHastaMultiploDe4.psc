    Algoritmo RestarHastaMultiploDe4
		//Definición de variables
		
		Definir num, resta Como Real
		Definir esMultiplo Como Logico
		Definir residuo Como Entero
		
		esMultiplo <- Falso
		
		Escribir "Ingrese un número inicial:"
		Leer num
		
		// Estructura Hacer-Mientras
		Repetir
			Escribir "Ingrese la cantidad a restar:"
			Leer resta
			
			num <- num - resta
			Escribir "El valor actual es: ", num
			
			residuo <- num MOD 4
			
			Si residuo == 0 Entonces
				esMultiplo <- Verdadero
				Escribir "¡Éxito! ", num, " es múltiplo de 4."
			Sino
				esMultiplo <- Falso
				Escribir num, " no es múltiplo de 4. Continúa restando."
			FinSi
			
		Hasta Que esMultiplo == Verdadero
		
		Escribir "Resultado final: ", num
FinAlgoritmo

