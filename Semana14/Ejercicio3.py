def evaluar_notas(notas):
    promedio = sum(notas) / len(notas)
    print(f"El promedio es: {promedio:.2f}")

    if promedio >= 6.0:
        print("El grupo aprueba.")
    else:
        print("El grupo reprueba.")


# Ejemplo con 5 notas
mis_notas = [7, 8, 5, 9, 6]
evaluar_notas(mis_notas)
