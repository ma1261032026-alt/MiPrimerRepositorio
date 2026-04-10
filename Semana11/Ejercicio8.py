# Bloque de 3 lineas
texto_8 = """Linea uno del fragmento 
esta es la segunda con letra a 
y la tercera para dividir"""

# Cuenta letras "a"
total_a = texto_8.count("a")

# Divide por saltos de linea
lista_oraciones = texto_8.splitlines()
print(f"Total 'a': {total_a}, Lista: {lista_oraciones}")
