# Ejercicio 5: Privacidad
nombre_completo = input("Ingrese su nombre completo (Nombre y Apellido): ")

# Convertir a lista y usar slicing con paso negativo para invertir (Apellido primero)
palabras = nombre_completo.split()
lista_invertida = palabras[::-1]

# Bucle anidado para formatear
resultado_final = []

for palabra in lista_invertida:
    letras_con_puntos = ""
    for letra in palabra:
        letras_con_puntos += letra + "."

    # Quitamos el último punto de la palabra para estética y agregamos a la lista
    resultado_final.append(letras_con_puntos.strip("."))

# Imprimir con separación clara entre apellido y nombre
print(" / ".join(resultado_final))
