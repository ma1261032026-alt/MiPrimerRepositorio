def transformar_validando(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"  # Aquí manejamos el error


# Prueba
print(transformar_validando("Sistemas", 5))
