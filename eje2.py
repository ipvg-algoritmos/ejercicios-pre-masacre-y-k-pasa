textoo = input("Ingrese una cadena de texto: ")
vocales = set("aeiouAEIOU")
c_vocales = 0
c_consonantes = 0

for caracter in textoo:
    if caracter.isalpha():
        if caracter in vocales:
            c_vocales += 1
        else:
         c_consonantes += 1

print("Cantidad vocales:", c_vocales)
print("Cantidad consonantes:", c_consonantes)