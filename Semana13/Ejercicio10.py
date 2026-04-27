total = 0
validos = []
while total <= 100:
    n = int(input("Suma un número: "))
    if n >= 0:
        total += n
        validos.append(n)

for v in validos:
    print(f"Sumado: {v}")
print(f"Total: {total}")
