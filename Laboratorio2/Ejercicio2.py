def mostrar_transformacion(palabra, numero):
    if numero == 1:
        print(palabra.upper())
    elif numero == 2:
        print(palabra.lower())
    elif numero == 3:
        print(palabra.capitalize())


# Llamada a la funcion
mostrar_transformacion("Hola", 1)
