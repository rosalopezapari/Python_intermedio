"""
*Ejercicio CONTROL_ACCESO:* Control de Acceso con Intentos (Bucle while y break)
Escribe un programa que simule el acceso a una cuenta personal mediante una contraseña previamente definida (por ejemplo, "python123").
- El usuario tiene un máximo de 3 intentos para ingresar la clave correcta.
- Si ingresa la contraseña correcta, el programa debe mostrar "Acceso concedido" y terminar inmediatamente con break.
- Si se equivoca, debe mostrar cuántos intentos le quedan.
- Si agota los 3 intentos sin éxito, debe imprimir "Cuenta bloqueada por seguridad".
"""
contraseña_correcta = "python123"
intentos_max = 3

for intento in range(1, intentos_max + 1):
    clave = input(f"Intento {intento} de {intentos_max}. Ingresa la contraseña: ")
    
    if clave == contraseña_correcta:
        print("Acceso concedido")
        break
    else:
        intentos_restantes = intentos_max - intento
        if intentos_restantes > 0:
            print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos.")
        else:
            print("Cuenta bloqueada por seguridad")