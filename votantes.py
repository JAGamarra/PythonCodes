# LIBRERÍAS IMPORTADAS
import os, time

# FUNCIONES LIBRERÍAS
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# VARIABLES GLOBALES ---->
listaVotantes = []
accesoRegistrado = {"user":"register", "password":"register@"} # ACCESS DATA TO SIGN IN AS A REGISTER
intentos =  3 # NOT IN USE

# SE DEFINEN LAS CLASES PERSONA Y VOTANTES ---->
class Persona:

    def __init__(self, cedula, nombre, apellido, edad):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


class Votantes(Persona):

    def __init__(self, cedula, nombre, apellido, edad, ciudadVotacion, puestoVotacion, mesaVotacion):
        Persona.__init__(self, cedula, nombre, apellido, edad)
        self.__ciudadVotacion = ciudadVotacion
        self.__puestoVotacion = puestoVotacion
        self.__mesaVotacion = mesaVotacion


    def entregarDatos(self):
        print(f" Cedula: {self.cedula}")
        print(f" Nombre: {self.nombre}")
        print(f" Apellido: {self.apellido}")
        print(f" Edad: {self.edad}")
        print(f" Ciudad de votacion: {self.__ciudadVotacion}")
        print(f" Puesto de votacion: {self.__puestoVotacion}")
        print(f" Mesa de votacion: {self.__mesaVotacion}")
    

# FUNCIONALIDADES ---->
def registrarVotante():
    clear() # CLEAR AQUÍ <<<<
    print("\n\nRegistro de votante\n")
    cedula = int(input("Ingrese cédula del votante: "))
    nombre = input("Ingrese nombre del votante: ")
    apellido = input("Ingrese apellido del votante: ")
    edad = int(input("Ingrese edad del votante: "))
    lugarVotacion = input("Ingrese lugar de votacion: ")
    puestoVotacion = input("Ingrese puesto de votacion: ")
    mesaVotacion = input("Ingrese mesa de votacion: ")
    objVotante = Votantes(cedula, nombre, apellido, edad, lugarVotacion, puestoVotacion, mesaVotacion)
    listaVotantes.append(objVotante)

    print("\n¡Registro exitoso!")
    os.system("read -p 'Press Enter to continue...' var")
    register()


def listarVotantes():
    clear() # CLEAR AQUÍ <<<<
    print("\nListado de votantes: ")
    indice = 1
    for objetoVotante in listaVotantes:
        print("\n")
        print(f"Votante N° {indice}")
        objetoVotante.entregarDatos()
        indice += 1
    print("\n")
    os.system("read -p 'Press Enter to continue...' var")
    register()


def consultarVotante():
    clear() # CLEAR AQUÍ <<<<
    encontrado = False
    print("\nConsulta de votante. ")
    cedula = int(input("Ingrese cédula del votante a consultar: "))
    print("\n")
    for objetoVotante in listaVotantes:
        if (cedula == objetoVotante.cedula):
            print("¡Encontrado!\n")
            objetoVotante.entregarDatos()
            encontrado = True
    if not encontrado: print("\nVotante no registrado en nuestra BBDD\n")
    print("\n")
    os.system("\nread -p 'Press Enter to continue...' var")



# TIPOS DE USUARIO ---->
def votante():
    try:
        clear() # CLEAR AQUÍ <<<<
        print("\n")
        print("|****************************|")
        print("|**|         Menú         |**|")
        print("|**|       Votantes       |**|")
        print("|****************************|")
        print("")
        print("Selecciona una de las siguientes opciones:");
        print("1.- Consultar datos")
        print("2.- Votar") # NO IMPLEMENTADO, DOESN'T WORK!
        opc = int(input("Ingrese opción: "))

        if (opc == 1):
            consultarVotante()
        elif (opc == 2):
            print("OUT OF SERVICE, NOT COMPLETED YET!")
        else:
            print("Opción incorrecta.")
    except:
        print("\nWoops! Algo ha ido mal...\n")


def register():
    try:
        clear() # CLEAR AQUÍ <<<<
        print("\n")
        print("|****************************|")
        print("|**|         Menú         |**|")
        print("|**|      Registrador     |**|")
        print("|****************************|")
        print("")
        print("Selecciona una de las siguientes opciones:");
        print("1.- Registrar votante")
        print("2.- Actualizar datos votante")
        print("3.- Consultar votante ")
        print("4.- Listar todos los votantes ")
        print("5.- Volver al menú principal")
        opc = int(input("Selecciona opción: "))

        if (opc == 1):
            registrarVotante()
        elif (opc == 2):
            pass
        elif (opc == 3):
            consultarVotante()
        elif (opc == 4):
            listarVotantes()
        elif(opc == 5):
            main()
    except:
        print("\nWoops! Algo ha ido mal...\n")


# FUNCIÓN PRINCIPAL ---->
def main():
    """
        Documentación aquí. (Si tan solo hubiera una...)
    """
    while True:
        try:
            clear() # CLEAR AQUÍ <<<<
            print("\n")
            print("|****************************|")
            print("|**|      Bienvenidos     |**|")
            print("|**|          Al          |**|")
            print("|**|         Menú         |**|")
            print("|****************************|")
            print("")
            print("Seleccione una de las siguientes opciones:");
            print("1.- Ingresar como votante")
            print("2.- Ingresar como registrador")
            print("3.- Salir del menú")
            opc = int(input('Selecciona opción: '))

            if (opc == 1):
                votante()

            elif (opc == 2):
                print("\n\nPor favor, ingrese para acceder como registrador: ")
                #user = input("Ingrese usuario: ")
                #passw = input("Ingrese contraseña: ")
                if (accesoRegistrado.get('user') == "register") and (accesoRegistrado.get('password') == "register@"):
                    register()
                else:
                    print("\nDatos erróneos.")

            elif (opc == 3):
                print("\nSaliste del menú")
                break

            else:
                print("\nOpción inválida. Intenta nuevamente.")
                time.sleep(1.5)

        except:
            print("\nWoops! Algo ha ido mal...\n")

if __name__ == '__main__':
    main();