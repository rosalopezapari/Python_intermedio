# control de flujo
## condicionles
### la sentencia if 
esta sentencia al igual que en otros lenguaje de programacion en su escritura debemos añadir una 'expresion de comparacion', terminando en dos puntos ´´´python
tempertatura
temperatura > 20 .


en este caso solo se ejecutara el bloque 

´´´python 
tem:int=20
if temp>35:
print ("temperatura alta")
else .
print

podriiiamos tener muchas condicionales, lo que se llamaria tecnicamente **condiciones anidadas**
´´´ python
temp int=20
if temp < 20:
if temp < 10:
print("nivel azul mucho frio")
else:
print("nivel verde normal")
else
if temp < 30:
print("nivel naranja")
else:
  print ("nivel rojo")
´´´
python ofrece una mejora en la escritura de condiciones anidadas, para ello podemos usar la sentencia 
´´´ python
temp int=20
if temp < 20:
if temp < 10:
print("nivel azul mucho frio")
else:
print("nivel verde normal")
else
elif temp < 30:
print("nivel naranja")
else:
  print ("nivel rojo")
´´´
### sentecia match-case
esta es una nueva sentencia condicional,similar a los if animados :
´´´python 
vocal:str="a"
match vocal:
case"a":
print ("es una vocal")
case "e"
print ("es una vocal")
case"i":
print ("es una vocal")
case "o"
 print ("es una vocal")
 case "u"
 print ("es una vocal")

case_:
print("es una constante")


vocal:str=input("ingrese una letra: ")
match vocall:
case "a"/"e"/"i"/"o"/"u":
print ("es una vocal")
case _:
print ("es una constante")
´´´´
## bucles
### la sentencia while 
es el primer mecanismo que exixte en python para repetir instrucciones. la sementica tras esta sentencia es :´Mientras se cumpla la condicion has algo´.
ejemplo:
´´´python 
salir:str="N"
while salir =="N":
print ("Hol que taal")
salir=input("deseas sair (S/N): ")
print("adios")
´´´

se piede cortar la ejecucion de un while 
pregunta = "¿Cuánto es 5 + 7?"
respuesta_correcta = "12"

oportunidades = 3

while oportunidades > 0:
    print(f"\nTienes {oportunidades} oportunidades")
    respuesta = input(f"{pregunta} ")
    
    if respuesta == respuesta_correcta:
        print("Correcto")
        break
    else:
        oportunidades = oportunidades - 1
        if oportunidades > 0:
            print("Incorrecto. Intenta de nuevo")
        else:
            print(f"Se acabaron tus intentos. La respuesta correcta era: {respuesta_correcta}")