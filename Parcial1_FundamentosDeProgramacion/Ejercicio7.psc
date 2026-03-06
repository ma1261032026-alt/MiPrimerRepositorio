Algoritmo  Ejercicio7
    
	Definir n1, n2, prod, coc Como Real
    
	Escribir "Ingrese el primer número:"
    leer n1
	
	Escribir "Ingrese el segundo número:"
    leer n2
	
	prod <- n1 * n2
    Si n2 <> 0 Entonces
        coc <- n1 / n2
        Escribir "El producto es: ", prod
        Escribir "El cociente es: ", coc
    Sino
        Escribir "El producto es: ", prod
        Escribir "Error: No se puede dividir entre cero."
    FinSi
	
FinAlgoritmo
