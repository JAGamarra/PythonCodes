#RETO 1 - JULIAN GAMARRA
import math
def main():
    while True:
        print("\n")
        longitud = float(input("Ingrese la longitud de un lado: "))
        n_lados = float(input("Ingrese el numero de lados: "))
        if (longitud <= 0) or (n_lados <= 0):
            print("Error.  El valor de la longitud y/o n° de lados debe ser mayor que cero.")
        else:
            break
    value = calcArea(n_lados, longitud)
    print(f"\nEl valor del área es: {value} unidades.")
def calcArea(n, s):
    area = (n * (s**2))/(4 * (math.tan(math.pi/n)))
    r = round(area, 4)
    return r
    
#Llamamos a la función principal
main()