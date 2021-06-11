def readint(prompt, min, max):
    while True:
        try:
            number = int(input(prompt))
            if number < -min or number > max:
                raise Exception("Error: Fuera de rango")
            else:
                return number
        except ValueError:
            print("Error: entrada incorrecta")
        except Exception:
            print(Exception)


v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)