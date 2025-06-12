numeroos = []
while True:
    numero = float(input("Ingresa un numero: "))
    if numero < 0:
     break
    numeroos.append(numero)

if numeroos:
    print("numero mayor: ", max(numeroos))
    print("numero menor: ", min(numeroos))
else:
    print("numero invalido")