class Vehiculo:

    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False


    def propiedades(self):
        print(f'Vehiculo marca: {self.marca}, modelo: {self.modelo}')
    


class VehiculoElectrico:

    def __init__(self, autonomia) -> None:
        self.autonomia = autonomia


class MotoElectrica(VehiculoElectrico, Vehiculo):

    def __init__(self, autonomia, marca, modelo) -> None:
        VehiculoElectrico.__init__(self, autonomia)
        Vehiculo.__init__(self, marca, modelo)
        self.ruedas = 2
    
    def mostrar(self):
        print(
            f"""
            Marca: {self.marca},
            Modelo: {self.modelo},
            Autonomia: {self.autonomia}
            Ruedas: {self.ruedas}
            """
        )

scooter = MotoElectrica(120, "Honda", "KF125")

scooter.mostrar()


#####################################3
lista = []
if lista == []:
    print (True)