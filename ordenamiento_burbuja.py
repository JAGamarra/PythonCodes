miLista = [8, 10, 6, 2, 4] # lista para ordenar
cambio = True # lo necesitamos verdadero (True) para ingresar al bucle while

while cambio:
    cambio = False # No hay cambios hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            cambio= True # Ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)