from usuario import Usuario
from estacionamiento import Estacionamiento
from vehiculo import Compacto, Todoterreno, Furgoneta

geovani = Usuario()
parking = Estacionamiento(30)
compact = Compacto()
todoterreno = Todoterreno()
furgoneta = Furgoneta()

def main_menu() -> None:
    print("Elija una opcion para continuar")
    print("1- Registro")
    print("2- Ingreso")
    escogido = int(input())
    try:
        if(escogido == 1):
            geovani.sign_in()
            main_menu()
        else:
            if(escogido == 2):
                geovani.login()
            else:
                print("Error, ingresa otro valor(1 o 2)")
                main_menu()
    except:
        print("El valor debe ser un entero.")
        main_menu()

print("Elija una opcion para continuar")
print("1- Registro")
print("2- Ingreso")
escogido = int(input())
try:
    if(escogido == 1):
        geovani.sign_in()
        main_menu()
    else:
        if(escogido == 2):
            geovani.login()
            parking.menu()
        else:
            print("Error, ingresa otro valor(1 o 2)")
            main_menu()
except:
    print("El valor debe ser un entero.")
    main_menu()
