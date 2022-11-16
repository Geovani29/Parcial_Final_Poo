class Vehiculo():
    def __init__(self) -> None:
        self.tipo = int
        self.valor_parking = int

class Compacto(Vehiculo):
    def __init__(self) -> None:
        self.valor_parking = 10

class Todoterreno(Vehiculo):
    def __init__(self) -> None:
        self.valor_parking = 15

class Furgoneta(Vehiculo):
    def __init__(self) -> None:
        self.valor_parking = 12