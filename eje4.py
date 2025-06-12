n1 = []

print("Ingresa numeros (negativo termina)")
while True:
    try:
        numero = float(input("Número: "))
        if numero < 0:
            break
        n1.append(numero)
    except ValueError:
        print("ingresa un número que sea válido")

if n1:
    promedio = sum(n1) / len(n1)
    print("El promedio es:", promedio)
else:
    print("números invalidos")