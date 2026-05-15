# Ejercicio 1: Clasificación de Paquetes
tracking = input("Ingrese el código de rastreo (AÑO-CATEGORÍA-PAÍS): ")

# Validación de seguridad
if not tracking:
    print("Error: La entrada está vacía. Finalizando programa.")
    exit()

# Extracción de la sección central (Categoría) usando Slicing
# Formato esperado: 2024-TECNOLOGIA-ES
partes = tracking.split("-")
if len(partes) == 3:
    categoria = partes[1]
    print(f"Categoría extraída: {categoria}")
else:
    # Intento de slicing si no hay guiones claros
    categoria = tracking[5:-3]
    print(f"Categoría extraída (slicing): {categoria}")

# Operador Ternario para determinar la ruta
resultado = "Ruta Local" if tracking.endswith("SV") else "Ruta Internacional"
print(resultado)
