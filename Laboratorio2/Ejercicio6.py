def transformar_y_contar(texto, numero):
    # Primero transformamos
    if numero == 1:
        resultado = texto.upper()
    elif numero == 2:
        resultado = texto.lower()
    elif numero == 3:
        resultado = texto.capitalize()
    else:
        resultado = texto

    # Luego contamos
    cantidad = len(resultado)
    return resultado, cantidad


# Probamos
texto_final, total = transformar_y_contar("Python es divertido", 1)
print(f"Texto: {texto_final} | Caracteres: {total}")
