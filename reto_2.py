#RETO 2 JULIÁN GAMARRA
def calculoImpuesto(informacion: dict) -> float:

    estado = int(informacion.get("estado"))
    ingreso = float(informacion.get("ingreso"))
    imp_total = 0

    #SI ES SOLTERO
    if (estado == 0):
        if (ingreso > 0 and ingreso <= 9950):
            imp_total = ingreso * 0.10

        elif (ingreso >= 9951 and ingreso <= 40525):
            imp_total = (9950 * 0.10) + ((ingreso - 9950) * 0.12)

        elif (ingreso >= 40526 and ingreso <= 86375):
            imp_total = (9950 * 0.10) + ((40525 - 9950) * 0.12) + (((ingreso - 9950) - 30575) * 0.22)


    #SI ES CASADO CON DECLARACIÓN CONJUNTA
    elif (estado == 1):
        if (ingreso > 0 and ingreso <= 19900):
            imp_total = ingreso * 0.10

        elif (ingreso >= 19901 and ingreso <= 81050):
            imp_total = (19900 * 0.10)  + ((ingreso - 19900) * 0.12)

        elif (ingreso >= 81051 and ingreso <= 172750):
            imp_total = (19900 * 0.10) + ((81050 - 19900) * 0.12) + (((ingreso - 19900) - (81050 - 19900)) * 0.22)



    #CASADO QUE DECLARA POR SEPARADO
    elif (estado == 2):
        if (ingreso > 0 and ingreso <= 9950):
            imp_total = ingreso * 0.10

        elif (ingreso >= 9951 and ingreso <= 40525):
            imp_total = ((9950 * 0.10) + ((ingreso - 9950) * 0.12))

        elif (ingreso >= 40526 and ingreso <= 86375):
            imp_total = (9950 * 0.10) + ((40525 - 9950) * 0.12) + (((ingreso - 9950) - (40525 - 9950)) * 0.22)



    #SI ES JEFE DE FAMILIA
    elif (estado == 3):

        if (ingreso > 0 and ingreso <= 14200):
            imp_total = ingreso * 0.10

        elif (ingreso >= 14201 and ingreso <= 54200):
            imp_total = (14200 * 0.10) + ((ingreso - 14200) * 0.22)

        elif (ingreso >= 54201 and ingreso <= 86350):
            imp_total = (14200 * 0.10) + ((54200 - 14200) * 0.12) + ((ingreso - 14200) - (54200 - 14200) * 0.22)


    return round(imp_total, 2)