"""
funcion_a -> Función principal (decoradora)
funcion_b -> Función a decorar
funcion_c -> Función decorada

funcion_a(funcion_b) -> funcion_c
"""

def funcion_a(funcion_b):

    
    def funcion_c(*args, **kwargs):
        print("<<< Vamos a hacer un cálculo.")

        funcion_b(*args, **kwargs)

        print("<<< Fin del programa.")



    return funcion_c


@funcion_a
def saludar():
    print("Hola, estamos practicando funciones decoradoras...")


@funcion_a
def potencia(base, expo):
    print(pow(base, expo))


# saludar()
potencia(base=5, expo=3)