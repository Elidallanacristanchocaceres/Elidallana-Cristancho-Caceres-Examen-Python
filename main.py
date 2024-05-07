import ejerciciotres.productos as ep

def mainMenu(op):
    
    Title="""
    ***********************
    * REGISTRAR PRODUCTOS *
    ***********************
"""

    mainMenuOp = "\n1. Registro productos "

    if (op != 1):
        print(Title)
        print(mainMenuOp)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print('La opcion que ingreso es erronea :')
            mainMenu(0)
        else:
            match (opcion):
                case 1:
                    ep.registro()
                case _:
                    print('La opcion ingreseda no se encuentra. Ingresa otra : ')
                    mainMenu(0)

if __name__ == '__main__': 
    mainMenu(0)