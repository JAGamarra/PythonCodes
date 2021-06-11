import math

def areaPoligono(n:float, s:float) -> str:
    area = (n * (s**2))/(4 * (math.tan(math.pi/n)))
    area = round(area, 4)
    salida = f"El área calculada es {area}"
    return salida
