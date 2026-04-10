# Nombre de archivo
archivo = "Saira.txt"

# Remueve sufijo ".txt" y prefijo "ING." (Si existiera)
# Minusculas

final = archivo.removesuffix(".txt").removeprefix("ING.").lower()
print(final)
