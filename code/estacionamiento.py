from espacios import Espacios
from vehiculo import Compacto, Todoterreno, Furgoneta
class Estacionamiento(Espacios):
    def __init__(self, cupos: int) -> None:
        self.horario = list
        self.cantidad = cupos
        self.money = int
        
    def cobrar(self):
        print("Tipo de vehiculo")
        print("1- compacto")
        print("2- todoterreno")
        print("3- furgoneta")
        option = int(input())
        if (option == 1):
            self.money = Compacto.valor_parking
            self.min_hor_dia()
        else:
            if (option == 2):
                self.money = Todoterreno.valor_parking
                self.min_hor_dia()
            else:
                if (option == 3):
                    self.money = Furgoneta.valor_parking
                    self.min_hor_dia()
                else:
                    print("Valor incorrecto, ingrese otro.")
                    self.cobrar()