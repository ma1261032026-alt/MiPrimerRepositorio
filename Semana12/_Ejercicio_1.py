entradaDeDatos = input("Ingrese un texto: ")


def validarMayusculas(entradaDeDatos):
    validar = entradaDeDatos.isupper()
    return validar


resultado = validarMayusculas(entradaDeDatos)
print(f"¿El texto esta todo en mayusculas?: {resultado}")
