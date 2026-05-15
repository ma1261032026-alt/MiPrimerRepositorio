# Ejercicio 4: Auditoria de Registros (Control de Flujo)
# Auditoría de 50 registros (1 a 50)

for id_registro in range(1, 51):
    # Filtro de Omisión: Múltiplos de 3 (corruptos)
    if id_registro % 3 == 0:
        continue

    # Protocolo de Parada: Brecha de seguridad en 42
    if id_registro == 42:
        print("!!! Brecha de seguridad detectada en ID 42. Deteniendo proceso.")
        break
    print(f"Procesando registro ID: {id_registro}")
