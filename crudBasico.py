import os, sys, time

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def create(tarea):
    clear()
    id = input("Ingrese un ID único para esta tarea: ")
    descripcion = input("Ingrese una descripción para la tarea: ")
    estado = "Pendiente"
    tiempo = int(input("Ingrese el tiempo aprox. en horas que tomará realizar esta tarea: "))

    tareaNueva = {"descripcion": descripcion, "estado": estado, "tiempo": tiempo}
    #con dict_name.update({"key":value}) se puede crear un nuevo par clave, valor en un diccionario
    tarea[id] = tareaNueva

    return tarea


def read(tarea):
    try:
        id = input("Ingrese el ID de la tarea a revisar: ") 
        desc = tarea[id]["descripcion"]
        estado = tarea[id]["estado"]
        tiempo = tarea[id]["tiempo"]
        d = tarea.get(id).get("descripcion")
        print(d)
        print("\n<<---------------------")
        print("ID: ", id)
        print("Descripción: ", desc)
        print("Estado: ", estado)
        print("Tiempo aprox.: ", tiempo)
        print("--------------------->>")
        print("Presione 'Enter' para continuar...")
        sys.stdin.read(1)

    except:
        print("ID no existente.")
        print("Será redireccionado al menu principal...")
        time.sleep(1.5)
    

def update(tarea):
    id = input("Ingrese el ID de la tarea a actualizar: ")
    desc = input("Ingrese la nueva descripción de la tarea: ")
    tim = int(input("Ingrese el tiempo aprox. en horas que tomará realizar esta tarea: "))
    opc = int(input("1. Pendiente  2. En curso  3. Completado \nIngrese su opción:"))
    if (opc == 1):
        status = "Pendiente"
    elif (opc == 2):
        status = "En curso"
    elif (opc == 3):
        status = "Completado"
    else:
        print("Opción errónea.")
        time.sleep(1.5)
        return tarea
    
    tarea[id]["descripcion"] = desc
    tarea[id]["tiempo"] = tim
    tarea[id]["estado"] = status
    return tarea


def delete(tarea):
    id = input("Ingrese el ID de la tarea a borrar: ")
    del tarea[id]
    return tarea
    

def main():

    tareas = {"01":{"descripcion":"Ir de compras", 
                    "estado":"Pendiente",
                    "tiempo":3},
              "02":{"descripcion":"Podar el cespéd", 
                    "estado":"Pendiente",
                    "tiempo":1}}
                    
    while True:
        print("\n <---- ADMINISTRADOR DE TAREAS ----> ")
        print("1. Crear nueva tarea")
        print("2. Leer una tarea")
        print("3. Actualizar una tarea")
        print("4. Eliminar una tarea")
        print("5. Salir del administrador.")
        try:
            opcion = int(input("Ingrese la opción: "))
            if (opcion == 1):
                tareas = create(tareas)
            elif (opcion == 2):
                read(tareas)
            elif (opcion == 3):
                update(tareas)
            elif (opcion == 4):
                delete(tareas)
            elif (opcion == 5):
                print("\nGracias por usar nuestros servicios.\n\n")
                break
            else:
                print("\nAcción equivocada. Intente nuevamente.")
                time.sleep(1.5)
                clear()
        except:
            print("\n¡Ups! Ha ocurrido un error.")
            time.sleep(1)


#<<<<<----------------------- LLAMADA A LA FUNCIÓN PRINCIPAL >>>
main()