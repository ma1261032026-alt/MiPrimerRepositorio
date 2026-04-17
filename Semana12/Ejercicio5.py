# Ejercicio 5: Calculadora que no se cierra hasta decir 's'
continuar = "si"

while continuar.lower() == "si":
    n1 = int(input("\nPrimer número: "))
    n2 = int(input("Segundo número: "))
    op = input("Operación (+, -, *, /): ")

    if op == "+":
        print("Suma:", n1 + n2)
    elif op == "-":
        print("Resta:", n1 - n2)
    elif op == "*":
        print("Multiplicación:", n1 * n2)
    elif op == "/":
        print("División:", n1 / n2) if n2 != 0 else print("Error: Div por 0")

    continuar = input("\n¿Quieres hacer otra cuenta? (si/no): ")

print("Calculadora finalizada.")
