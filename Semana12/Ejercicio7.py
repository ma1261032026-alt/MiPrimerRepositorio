# Ejercicio 7: Monto de compra
compra = int(input("Monto total: "))

if compra > 100:
    print("Total con 20% desc:", compra * 0.80)
elif 50 <= compra <= 100:
    print("Total con 10% desc:", compra * 0.90)
else:
    print("Total sin descuento:", compra)
