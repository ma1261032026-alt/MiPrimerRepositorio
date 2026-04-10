# Texto numérico "42"
num = "42"
# Rellena con ceros a la izquierda hasta longitud 5
rellenado = num.zfill(5)
# Verifica si termina con "2"
valida = rellenado.endswith("2")
print(f"Resultado: {rellenado}, ¿Termina en 2?: {valida}")
