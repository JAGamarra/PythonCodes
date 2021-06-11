def establecerTablero(info:dict) -> dict:
    
    # INFORMACIÓN DICCIONARIO
    nick = info.get("nick")
    t1 = info.get("ubicaciones").get("T1")
    t2 = info.get("ubicaciones").get("T2")
    t3 = info.get("ubicaciones").get("T3")

    # VARIABLES AUXILIARES
    error = False # CAMBIA SI HAY UN ERROR
    dict_salida = {} # SE ALMACENA EL DICCIONARIO DE SALIDA
    tesorosErr = [] # SE ALMACENAN LAS UBICACIONES FALLIDAS
    tablero = [["TO" for _ in range(6)] for _ in range(6)] #CREAMOS LA MATRIZ TABLERO CON 'TO'
    
    # PARA UBICACION T1
    try:
        if t1[0] < 0 or t1[1] < 0:
            raise Exception # SI LOS INDICES SON NEGATIVOS SE LANZA UNA EXCEPCION

        if t1[2] == 'D': # DERECHA
            if tablero[t1[0]][t1[1]] == 'TO' and tablero[t1[0]][t1[1] + 1] == 'TO' and tablero[t1[0]][t1[1] + 2] == 'TO':
                tablero[t1[0]][t1[1]] = 'T1'
                tablero[t1[0]][t1[1] + 1] = 'T1'
                tablero[t1[0]][t1[1] + 2] = 'T1'
            else:
                raise Exception # SI EL TABLERO NO ESTÁ EN BLANCO SE LANZA UNA EXCEPCION

        elif t1[2] == 'A': # ABAJO
            if tablero[t1[0]][t1[1]] == 'TO' and tablero[t1[0] + 1][t1[1]] == 'TO' and tablero[t1[0] + 2][t1[1]] == 'TO':
                tablero[t1[0]][t1[1]] = 'T1'
                tablero[t1[0] + 1][t1[1]] = 'T1'
                tablero[t1[0] + 2][t1[1]] = 'T1'
            else:
                raise Exception # SI EL TABLERO NO ESTÁ EN BLANCO SE LANZA UNA EXCEPCION
    except:
        error = True
        tesorosErr.append('T1')

    # PARA UBICACION T2
    try:
        if t2[0] < 0 or t2[1] < 0:
            raise Exception # SI LOS INDICES SON NEGATIVOS SE LANZA UNA EXCEPCION

        if t2[2] == 'D': # DERECHA
            if tablero[t2[0]][t2[1]] == 'TO' and tablero[t2[0]][t2[1] + 1] == 'TO' and tablero[t2[0]][t2[1] + 2] == 'TO':
                tablero[t2[0]][t2[1]] = 'T2'
                tablero[t2[0]][t2[1] + 1] = 'T2'
                tablero[t2[0]][t2[1] + 2] = 'T2'
            else:
                raise Exception # SI EL TABLERO NO ESTÁ EN BLANCO SE LANZA UNA EXCEPCION

        elif t2[2] == 'A': # ABAJO
            if tablero[t2[0]][t2[1]] == 'TO' and tablero[t2[0] + 1][t2[1]] == 'TO' and tablero[t2[0] + 2][t2[1]] == 'TO':
                tablero[t2[0]][t2[1]] = 'T2'
                tablero[t2[0] + 1][t2[1]] = 'T2'
                tablero[t2[0] + 2][t2[1]] = 'T2'
            else:
                raise Exception # SI EL TABLERO NO ESTÁ EN BLANCO SE LANZA UNA EXCEPCION
    except:
        error = True
        tesorosErr.append('T2')

    # PARA UBICACION T3
    try:
        if t3[0] < 0 or t3[1] < 0:
            raise Exception # SI LOS INDICES SON NEGATIVOS SE LANZA UNA EXCEPCION

        if t3[2] == 'D': # DERECHA
            if tablero[t3[0]][t3[1]] == 'TO' and tablero[t3[0]][t3[1] + 1] == 'TO' and tablero[t3[0]][t3[1] + 2] == 'TO':
                tablero[t3[0]][t3[1]] = 'T3'
                tablero[t3[0]][t3[1] + 1] = 'T3'
                tablero[t3[0]][t3[1] + 2] = 'T3'
            else:
                raise Exception # SI EL TABLERO NO ESTÁ EN BLANCO SE LANZA UNA EXCEPCION

        elif t3[2] == 'A': # ABAJO
            if tablero[t3[0]][t3[1]] == 'TO' and tablero[t3[0] + 1][t3[1]] == 'TO' and tablero[t3[0] + 2][t3[1]] == 'TO':
                tablero[t3[0]][t3[1]] = 'T3'
                tablero[t3[0] + 1][t3[1]] = 'T3'
                tablero[t3[0] + 2][t3[1]] = 'T3'
            else:
                raise Exception # SI EL TABLERO NO ESTÁ EN BLANCO SE LANZA UNA EXCEPCION
    except:
        error = True
        tesorosErr.append('T3')

    
    if error: tablero = -1
    else: tesorosErr = 0

    dict_salida = {'nombreJugador':nick, 'tesorosErroneos':tesorosErr, 'tablero':tablero}

    return dict_salida



if __name__ == "__main__":
    infoPrueba1 = {
        "nick":"lucila",
        "ubicaciones":{
            "T1":[0, 0, "D"],
            "T2":[3, 0, "A"],
            "T3":[3, 3, "D"]
        }
    }

    infoPrueba2 = {
        "nick":"juanito",
        "ubicaciones":{
            "T1":[5, 0, "D"],
            "T2":[5, 2, "A"],
            "T3":[4, 4, "D"]
        }
    
    }

    infoPrueba3 = {
        "nick":"paco",
        "ubicaciones":{
            "T1":[-1, 0, "D"],
            "T2":[0, 2, "A"],
            "T3":[4, 4, "D"]
        }
    }

    infoPrueba4 = {
        "nick":"paco",
        "ubicaciones":{
            "T1":[1, 2, "A"],
            "T2":[4, 1, "D"],
            "T3":[3, 4, "A"]
        }
    }

    infoPrueba5 = {
        "nick":"paco",
        "ubicaciones":{
            "T1":[2, 2, "D"],
            "T2":[0, 4, "A"],
            "T3":[3, 2, "D"]
        }
    }

    print(establecerTablero(infoPrueba1))
    print("\n\n")
    print(establecerTablero(infoPrueba2))
    print("\n\n")
    print(establecerTablero(infoPrueba3))
    print("\n")
    print(establecerTablero(infoPrueba4))
    print("\n")
    print(establecerTablero(infoPrueba5))
    print("\n")
    # print(establecerTablero(infoPrueba6))
    # establecerTablero(infoPrueba1)