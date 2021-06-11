def analisisEstadistico(informacion:dict) -> dict:
    
    listaNotasA = list()
    listaNotasB = list()
    listaNotasC = list()
    peorA = " "
    peorB = " "
    peorC = " "
    mejorA = " "
    mejorB = " "
    mejorC = " "
    mayorA = -999
    mayorB = -999
    mayorC = -999
    menorA = 100
    menorB = 100
    menorC = 100

    for key in informacion: 
        notaA = informacion[key].get('Trabajo A')
        notaB = informacion[key].get('Trabajo B')
        notaC = informacion[key].get('Trabajo C')
##########################################################
        if notaA != None:
            listaNotasA.append(notaA)
            if notaA > mayorA:
                mayorA = notaA
                mejorA = key
            if notaA < menorA:
                menorA = notaA
                peorA = key
#########################################################
        if notaB != None:
            listaNotasB.append(notaB)
            if notaB > mayorB:
                mayorB = notaB
                mejorB = key
            if notaB < menorB:
                menorB = notaB
                peorB = key
##########################################################
        if notaC != None:
            listaNotasC.append(notaC)
            if notaC > mayorC:
                mayorC = notaC
                mejorC = key
            if notaC <= menorC:
                menorC = notaC
                peorC = key
    cantidadA = len(listaNotasA)
    cantidadB = len(listaNotasB)
    cantidadC = len(listaNotasC)
    totalA = sum(listaNotasA)
    totalB = sum(listaNotasB)
    totalC = sum(listaNotasC)

    promA = round((totalA / cantidadA), 2)
    promB = round((totalB / cantidadB),2)
    promC = round((totalC / cantidadC),2)

    dictResultado = {'Trabajo A': {'mejor':mejorA, 'mayor': mayorA, 'peor':peorA, 'menor':menorA, 'promedio': promA, 'cantidad': cantidadA, 'total':totalA},
                     'Trabajo B': {'mejor':mejorB, 'mayor': mayorB, 'peor':peorB, 'menor':menorB, 'promedio': promB, 'cantidad': cantidadB, 'total':totalB},
                     'Trabajo C': {'mejor':mejorC, 'mayor': mayorC, 'peor':peorC, 'menor':menorC, 'promedio': promC, 'cantidad': cantidadC, 'total':totalC}}

    return dictResultado




# dct1 = {'Gustavo':{'Trabajo A': 80, 'Trabajo B': 90},
#        'Ana':{'Trabajo A': 82, 'Trabajo C':100},
#        'Joaquín':{'Trabajo C':100}}

# dct2 = {'Gustavo':{'Trabajo A':60,'Trabajo B':70},
#         'Ana': {'Trabajo A':90,'Trabajo B':40},
#         'Luis': {'Trabajo A':95,'Trabajo B':100},
#         'Paola': {'Trabajo A': 0,'Trabajo C': 0},
#         'Caro': {'Trabajo C':50}}
# dct3 = {'Ana':    {'Trabajo A':50,'Trabajo B':100},
#         'Angela': {'Trabajo A':10,'Trabajo B':40},
#         'Andres': {'Trabajo A':55,'Trabajo B':99},
#         'Juan':   {'Trabajo A':60,'Trabajo C': 0},
#         'Paola':  {'Trabajo C':10}}

# print(analisisEstadistico(dct1))
# print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
# print(analisisEstadistico(dct2))
# print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
# print(analisisEstadistico(dct3))
