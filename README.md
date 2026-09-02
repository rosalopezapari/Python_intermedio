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
