# Ejercicio 3: Sensor loT(Match-Case y Listas)

lecturas = []

# Solicitar 5 lecturas
for i in range(5):
    temp = int(input(f"Ingrese la lectura de temperatura {i+1}: "))
    lecturas.append(temp)

# Iterar y evaluar
for t in lecturas:
    match t:
        case 0:
            print(f"Temperatura {t}: Alerta: Punto de Congelación")
        case 100:
            print(f"Temperatura {t}: Alerta: Punto de Ebullición")
        case _:
            # Operador ternario interno para el rango 10-30
            estado = "Estado: Estable" if 10 <= t <= 30 else "Estado: Crítico"
            print(f"Temperatura {t}: {estado}")
