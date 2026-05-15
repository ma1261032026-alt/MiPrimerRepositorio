# Ejercicio 2: Cobro Seguro(Uso de Decimal)

from decimal import Decimal, InvalidOperation

total = Decimal("0")

while True:
    entrada = input("Ingrese el precio del producto (o '0' para finalizar): ")

    try:
        monto = Decimal(entrada)

        if monto == 0:
            break

        total += monto

    except (ValueError, InvalidOperation):
        print(
            "Advertencia: El valor ingresado no es un número válido. Intente de nuevo."
        )

print(f"El total acumulado es: ${total:.2f}")
