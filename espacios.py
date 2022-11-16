class Espacios():
    def __init__(self) -> None:
        self.cantidad = int
        self.espacios = []

    def iniciar(self):
        for iter in range(self.cantidad):
            self.espacios.append("vacio")