while True:
    tabla = int(input("Número para la tabla (-1 para salir): "))
    if tabla == -1:
        break
    for i in range(1, 11):
        res = tabla * i
        if res > 20:
            print(f"{tabla} x {i} = {res}")
