# Tomar el texto "Su nombre"
texto_6 = "Saira"
# 2. Normalización fuerte (casefold)
normalizado = texto_6.casefold()
# Verificar si es solo alfabético (letras)
es_letra = normalizado.isalpha()
print(f"¿Es alfabético?: {es_letra}")
