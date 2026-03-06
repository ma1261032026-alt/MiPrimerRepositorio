Funcion respuesta <- validar ( usuario, pass)
Escribir "validar usuario"	
Si usuario == "SairaMelgar" Entonces 
	Si pass == "Saira" Entonces
		Escribir "Bienvenido"
		respuesta = verdadero 
 SiNo 
	Escribir "Fallo de password"
Fin Si

SiNo
	Escribir "Fallo de usuario"
 Fin Si 
FinFuncion
// funcion 
// encapsulacion -> siempre me va a dar la misma salida 
// va a crear algo que se llama scope


// las variables siempre tiene que tener sentido
// edad 32 funcion entero <- registrarpersona(edad)
// funcion entero <- registrar(xw)
// nombre en clave de las variables nombre de ex, nombres personajes, fechas...
// xw "Hola como estas"
// nomeclatura camelcase sneakcase
// glosario
// ADN
// ARN
// femur

Algoritmo bucleFor
	// Indica que vamos a repetir los pasos o un algoritmo en un numero de pasos definido
	
	// yo quiero utilizar la cuenta de correo 
	// pero si me equivoco mas de 4 veces
	// se loquea momentaneamente
	
	Definir increment Como Entero 
	
	Escribir "registrar usuario"
	leer usuario
	
	Escribir "registrar PASS"
	leer pass
	
	Definir i Como Entero 
	Para i <- 1 Hasta 5 Con Paso  1 Hacer 
			resultado = validar ( usuario , pass)
			Si resultado == Verdadero 
				Escribir "Bienvenida"
				Escribir "indicaciones"
			FinSi
			resultado = False 
	FinPara
	// for i  0;  instruccionalLogica i>20 ; 
	// i = i + 1 .....19 detener el bucle
	
	
	// funcion es una estructura de codigo 
	// que se puede repetir pero siempre se llama a la misma instancia 
	// vajo el mismo nombre
	
	// palabra re. si nos devuelve algo ()
	// argumentos :son las entradas de las funcines van entre parentesis y puede ser 
	// mas de una o ninguna.
	// caracteristicas -> el carro es rojo 
	//                        edad                  32
	//                       boleano              verdad o falso
	//                       objeto  :            es un objeto es aquella entidad
	//                                           en programacion que modela en base a las clases
	//                                           las caracteristicas de un objeto de la vida real
	
	
FinAlgoritmo
