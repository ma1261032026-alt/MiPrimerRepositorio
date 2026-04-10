# 1. Definimos la variable con tu nombre
texto = "Saira"

# 2. Convertimos a formato de título
texto_titulo = texto.title()

# 3. Reemplazamos el nombre por tu apellido Melgar
# Importante: Como usamos title(), la primera letra es mayúscula "Saira"
nuevo_texto = texto_titulo.replace("Saira", "Melgar")

# Mostramos los resultados
print(f"Paso 2 (Mayúsculas): {texto_titulo}")
print(f"Paso 3 (Reemplazo): {nuevo_texto}")
