def obtener_positivos(arreglo):
    nuevos_positivos = []
    for n in arreglo:
        if n > 0:
            nuevos_positivos.append(n)
    return nuevos_positivos


datos = [-5, 10, 0, 3, -1, 8]
resultado = obtener_positivos(datos)
print(f"Solo positivos: {resultado}")
