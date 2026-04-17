# Ejercicio 10: Login con límite de 3 intentos
usuario_real = "admin"
clave_real = "1234"
intentos = 3

while intentos > 0:
    user = input("\nUsuario: ")
    password = input("Contraseña: ")

    if user == usuario_real and password == clave_real:
        print("¡Acceso permitido!")
        break  # Esto rompe el bucle y sale
    else:
        intentos -= 1
        print(f"Incorrecto. Te quedan {intentos} intentos.")

if intentos == 0:
    print("Acceso bloqueado por seguridad.")
