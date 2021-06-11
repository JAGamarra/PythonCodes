# Docstring
# __doc__ Propiedad que tienen objetos documentables. 
# Documentar y testear funciones, clases, métodos, y módulos.



def factorial(n):

    """
        Function to calculate the factorial number of n

        Arguments:
        n (positive int)

        Returns the result of factorial (int)


        >>> factorial(3)
        6

        >>> factorial(5)
        120

    """

    if (n == 1):
        return 1
    
    return n * factorial(n-1)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod() # Testea las funciones. 