"""
Testear clases y/o métodos

>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120

>>> recursivo.factorial(13)
6227020800
"""

def fibonacci(number):
    """
    >>> fibonacci(12)
    144
    """

    if number == 1: return 1
    elif number == 0: return 0
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

class Recursivo:
    def factorial(self, number):
        if number == 1: return 1
        else:
            return number * self.factorial(number - 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # Testea las funciones. 