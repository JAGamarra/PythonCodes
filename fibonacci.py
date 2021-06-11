def fibonacci(limit):
    if (limit <= 0):
        return "Error"
    prevNumber = 0
    actNumber = 1
    nextNumber = 0
    fibonacciList = [0, 1]
    for _ in range(limit):
        nextNumber = prevNumber + actNumber
        prevNumber = actNumber
        actNumber = nextNumber
        fibonacciList.append(nextNumber)
    return fibonacciList

prueba = fibonacci(12)

print(prueba)