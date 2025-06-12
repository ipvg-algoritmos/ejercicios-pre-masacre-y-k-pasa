posi = nega = c = dp = ds = 0

for i in range(3):
    for j in range(3):
        x = int(input(f"[{i+1}][{j+1}]: "))
        if x > 0:
            posi += 1
        elif x < 0:
            nega += 1
        else:
            c += 1
        if i == j:
            dp += x
        if i + j == 2:
            ds += x

print(f"\nPositivos: {posi}, Negativos: {nega}, Ceros: {c}")

if dp > ds:
    print("Diagonal principal > Diagonal secundaria")
elif dp < ds:
    print("Diagonal principal < Diagonal secundaria")
else:
    print("Diagonales iguales")