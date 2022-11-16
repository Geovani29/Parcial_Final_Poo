from espacios import Espacios
from vehiculo import Compacto, Todoterreno, Furgoneta
c1 = Compacto()
c2 = Todoterreno()
c3 = Furgoneta()
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
            self.money = c1.valor_parking
            self.min_hor_dia()
        else:
            if (option == 2):
                self.money = c2.valor_parking
                self.min_hor_dia()
            else:
                if (option == 3):
                    self.money = c3.valor_parking
                    self.min_hor_dia()
                else:
                    print("Valor incorrecto, ingrese otro.")
                    self.cobrar()
        
    def menu(self) -> None:
        #self.iniciar()
        self.cobrar()

    def min_hor_dia(self) -> None:
        print("Necesita parquear por:")
        print("1-Minutos")
        print("2-Horas")
        print("3-Dias")
        option = int(input())
        if (option == 1):
            print("¿Cúantos minutos?")
            minutos = int(input())
            self.money = self.money*minutos
            self.pagaras()
        else:
            if (option == 2):
                print("¿Cúantas horas?")
                horas = int(input())
                self.money = self.money*horas*60
                self.pagaras()
            else:
                if (option == 3):
                    print("¿Cúantos dias?")
                    dias = int(input())
                    self.money = self.money*dias*60*24
                    self.pagaras()
                else:
                    print("Incorrecto, ingrese otro valor")
                    self.min_hor_dia()

    def pagaras(self):
        print(f"Debe pagar {self.money}")