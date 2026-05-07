def contar_adultos(edades):
    adultos = 0
    for edad in edades:
        if edad >= 18:
            adultos += 1
    return adultos


# Prueba con una lista de edades
edades_lista = [15, 22, 18, 30, 12, 17, 45]
print(f"Cantidad de personas mayores de edad: {contar_adultos(edades_lista)}")
