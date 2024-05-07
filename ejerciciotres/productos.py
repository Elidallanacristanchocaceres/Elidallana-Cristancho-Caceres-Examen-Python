import os
import json

def registro():
    id = int(input("Inrese el numero de identificacion : "))
    nombre = input("Cual es su nombre : ")
    valorUnitario = int(input("Ingrese el valor del producto : "))
    stockmin = int(input("Cual es el stock por minutos : "))
    stockmax = int(input("Ingresa el stockmax : "))
    valorUnitario = int(input("Ingresa el valor unitario : "))

    viveres ={
    'id' : id,
    'nombre' : nombre,
    'valorUnitario' : valorUnitario,
    'stockmin' : stockmin,
    'stockmax' : stockmax,
    'valorUnitario' : valorUnitario

    }


    print(f'id', id)
    print(f'nombre', nombre)
    print(f'valorUnitario', valorUnitario)
    print(f'stockmin', stockmin)
    print(f'stockmax', stockmax)
    print(f'valorUnitario', valorUnitario)

print("Los productos fueron registrados : ", registro)
