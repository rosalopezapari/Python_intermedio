## crear un programa de login que mientras quela persona no ponga el usuario /contraseña correcto la siga pidiendo esa informacion, si el usuario /contraseña son correctos entonces darle in mensaje de bienvenida y salir del programa

USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "1234"

while True:
    print("\n--- INICIAR SESIÓN ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    
    if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
        print("\n Bienvenido 🎉")
        break  # sale del bucle y termina el programa
    else:
        print("Usuario o contraseña incorrectos. Intenta de nuevo.")

print("Saliendo del programa...")