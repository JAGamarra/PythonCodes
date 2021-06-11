#Calcula números primos
def isPrime(num):
    if (num > 1):
        contador = 1
        suma = 0
        while (contador <= num):
            if (num % contador) == 0:
                suma += 1
            contador += 1

        if (suma <= 2):
            return True
        else:
            return False

for i in range(2, 20):
    if isPrime(i):
       print(i, end=" ")