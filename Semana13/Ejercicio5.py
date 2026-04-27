clave_real = "python123"
fallidos = []
while True:
    intento = input("Contraseña:")
    if intento == clave_real:
        print("Aceso correcto")
        break
    else:
        fallidos.append(intento)

for f in range(len(fallidos)):
    print(f"Fallo {f+1}: {fallidos[f]}")
