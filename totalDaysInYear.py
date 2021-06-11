#FUNCION PARA VERIFICAR SI UN AÑO ES BISIESTO O NO
def isYearLeap(year):
    if (year % 4 != 0):
        return False
    elif (year % 100 != 0):
        return True
    elif (year % 400 != 0):
        return False
    else:
        return True
        
#FUNCION QUE DEVUELVE CUANTOS DÍAS TIENE CIERTO MES
#(SOLO TIENE EN CUENTA EL AÑO BISIESTO PARA FEBRERO: MES 2)
def daysInMonth(year, month):
    contador = 0
    leapYear = isYearLeap(year)
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (leapYear and (month == 2)):
        return 29
    for numberOfMonth in months:
        if month == numberOfMonth:
            return days[contador] #DEVOLVEMOS LOS DÍAS QUE TIENE CADA MES CORRESPONDIENTE AL MES EN CUESTIÓN
        contador+=1

def dayOfYear(year, month, day):
    totalDays = 0
    #EL CICLO SE EJECUTA NÚMERO DE MESES - 1. YA QUE EL ÚLTIMO MES PUEDE ESTAR INCOMPLETO O NO TENER LOS 30/31 DÍAS.
    #POR ESO SE SUMAN EL NÚMERO DE DÍAS MÁS ABAJO
    for i in range(1, month):
        totalDays += daysInMonth(year, i) #ALMACENAMOS LOS DÍAS Y LOS VAMOS SUMANDO
    
    totalDays += day #
    return totalDays

print(dayOfYear(2000, 6, 11))