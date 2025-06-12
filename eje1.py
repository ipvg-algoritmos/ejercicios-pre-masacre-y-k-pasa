list_numero = [10, 24, 8, 14,30,12 ,18,20,3,27]
try:
    numero = int(input("ingresa un numero: "))
    if numero in list_numero:
        print(f"el numero {numero} esta en la posicion {list_numero.index(numero)}")
    else: 
        print("El numero no esta en la lista")
except ValueError:
    print("Error")