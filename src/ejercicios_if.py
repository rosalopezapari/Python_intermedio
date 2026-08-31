# 1.  escrba un programa que acepte la opcion de dos jugadores en piedra - papel o tijera
"""
-entrada: persona1=piedra,persona=papel
-salida:gana persona2, papel envuelvepiedra 

2. escribe un programa que acepte 3 numeros y calcule el minimo
- entrada: 7,4,8
-salida:4
"""

## 1. piedra papel o tijera

persona1 = input("jugador 1: ")
persona2 = input("jugador 2: ")

if persona1 == "piedra" and  persona2 == "piedra" :
    print("ninguno gana ")
elif persona1 == "piedra" and persona2 == "tijera":
    print("gana jugador 1")
elif persona1 == "papel" and persona2 == "piedra":
    print("gana jugador 1")
elif persona1 == "tijera" and persona2 == "papel":
    print("gana jugador 1")
else:
    print("gana jugador 2")


## 2. minimo de 3 numeros

a = int(input("numero 1: "))
b = int(input("numero 2: "))
c = int(input("numero 3: "))

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
