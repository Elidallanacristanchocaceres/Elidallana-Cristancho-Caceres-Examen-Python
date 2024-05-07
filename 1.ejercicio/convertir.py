def pesos_to_dollars(pesos):
    return pesos / 3944

def pesos_to_euros(pesos):
    return pesos / 4279

def euros_to_pesos(euros):
    return euros * 4279

def pesos_to_yen(pesos):
    return pesos / 26.30

def main():
    print("1. Convertir de pesos a dólares")
    print("2. Convertir de pesos a euros")
    print("3. Convertir de euros a pesos")
    print("4. Convertir de pesos a yenes")
    
    opcion = int(input("Escoge una de estas opciones (1/2/3/4): "))
    
    if opcion == 1:
        pesos = float(input("Digite la cantidad en pesos: "))
        print(f"{pesos} pesos equivalen a {pesos_to_dollars(pesos):.2f} dólares.")
    elif opcion == 2:
        pesos = float(input("Digite la cantidad en pesos: "))
        print(f"{pesos} pesos equivalen a {pesos_to_euros(pesos):.2f} euros.")
    elif opcion == 3:
        euros = float(input("Digite la cantidad en euros: "))
        print(f"{euros} euros equivalen a {euros_to_pesos(euros):.2f} pesos.")
    elif opcion == 4:
        pesos = float(input("Digite la cantidad en pesos: "))
        print(f"{pesos} pesos equivalen a {pesos_to_yen(pesos):.2f} yenes.")
    else:
        print("La opcion no es valida. Por favor seleccione una valida.")

if __name__ == "__main__":
    main()
