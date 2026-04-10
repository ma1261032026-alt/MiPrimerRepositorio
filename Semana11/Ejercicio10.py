# Cadena "Python2026"
Cadena_10 = "Python2026"

# Verifica si es alfanumerico
if Cadena_10.isalnum():
    # Minusculas y reemplaza el año por vacio
    limpio = Cadena_10.lower().replace("2026", "")
    print(limpio)
