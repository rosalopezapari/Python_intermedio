## 1. crear una lista de ingredientes ("camote","papa","ques","huevo") crear un programa que recorra con for los elementos de la lista y me retorne el valor y su indice del ingrediente "queso".

ingredientes:list[str]=["camote","papa","queso","huevo"]

for i in ingredientes:
    if i == "queso":

        print(f"el valor es: {i}")

        print(f" el indice es: {ingredientes.index (1) }")

## 2. del siguente texto "errar es umano dijo el pato bajandose de la gallina" encontrar el error ortografico y corregir con por el correcto.
texto = "errar es umano dijo el pato bajandose de la gallina"

palabras = texto.split()

for i in range(len(palabras)):
    if palabras[i] == "umano":
        palabras[i] = "humano"

nuevo_texto = ""
for p in palabras:
    nuevo_texto = nuevo_texto + p + " "

print ("Texto corregido:")
print (nuevo_texto)