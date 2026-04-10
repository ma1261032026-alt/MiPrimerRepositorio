# Tomar la palabra "CANTANDO"

palabra = "CANTANDO"

# 2. Convertir a minúsculas

min_palabra = palabra.lower()

# Eliminar sufijo "ando" y busca el índice de "t"

final_palabra = min_palabra.removesuffix("ando")
indice_t = final_palabra.find("t")
print(f"Palabra: {final_palabra}, Posición de 't': {indice_t}")
