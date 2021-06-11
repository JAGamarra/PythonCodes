def factorialNumber(number):
    if (number < 0): return None
    if (number < 2): return 1
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    return factorial

number = int(input("Type a number: "))

print(f"The {number} factorial is {factorialNumber(number)}")

"""
Factorial con función recursiva:

# Implementación recursiva de la función factorial

def factorial(n):
    if n == 1:    # la condición de terminación
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # 4 * 3 * 2 * 1 = 24

"""