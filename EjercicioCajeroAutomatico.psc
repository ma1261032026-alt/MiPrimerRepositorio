Algoritmo EjercicioCajeroAutomatico
	Definir cajero, cuentaDeAhorro, cantidadSaliente, Saldo, preguntar Como entero
	cuentaDeAhorrro = 1000
	numeroDeCuenta = 12345
	
	Escribir " bienvenido"
	Escribir " Actividad que desee realizar"
	Escribir " 1 para consultar"
	Escribir " 2 para extraer dinero de la cuenta de ahorro"
	
	Escribir " Escriba el numero de cuenta a operar"
	Leer preguntar // yo no quiero ser un uno mejor busco otra chamba
	
	si preguntar == 1
		Escribir " Escriba el numero de cuenta a operar"
		Leer preguntar // es valor de numero de cuentas
		si preguntar == numeroDeCuenta
			Escribir " Su saldo es " , cuentaDeAhorro
		FinSi
		Finsi
	
		si preguntar == 2
			Escribir " Escriba el numero de cuenta a operar"
			Leer preguntar // es valor de numero de cuentas
			si preguntar == numeroDeCuenta
				Escribir " Escriba el monto a extraer"
				Leer preguntar // es la cantidad a extraer
				
				// < = 
				si preguntar <= cuentaDeAhorro
					Saldo = cuentaDeAhorro - preguntar
					Escribir  "Procesando"
					Escribir " Su saldo actual es de" , Saldo 
					
                 Finsi
					
				FinSi
				
		Finsi
		
		
		
		
		
		
		// or o puedes llevar 
	// panes con cafe o chocolate
	
	// and puedes llevar carne y jamon
	
	// not mejor no
	
	
		// == si es igual
		// <> distinto
	
	
	
	
	// no pueden comenzar con
	// numero
	// signos a menos que sea _
	// no deben llevar espacio
	// Si es una calse siempre inicia con Mayusculas
	// es evitar el codigo espaguetti
	
FinAlgoritmo
