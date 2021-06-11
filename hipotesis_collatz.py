#HIPOTÉSIS DE COLLATZ

c0 = int(input("Ingresá un número mayor que cero: "))

i = 0
while c0 != 1:
    if (c0 % 2 == 0):
        c0 = int(c0 / 2)
    else:
        c0 = int((3 * c0) + 1)
    i+=1
    print(c0)
print(f"Pasos: {i}")