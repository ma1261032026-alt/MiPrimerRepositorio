def transformar_y_aplicar(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return texto


# Solicitamos datos
mi_texto = input("Escribe una frase: ")
mi_opcion = int(
    input("Elige una opcion (1: Mayusculas, 2: Minusculas, 3: Capitalizar): ")
)
# Llamamos a la función y mostramos el resultado
print("Resultado:", transformar_y_aplicar(mi_texto, mi_opcion))
