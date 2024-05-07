import os 

id = int(input("Ingrese el numero de identificacion : "))
nombres = input("Ingrese sus nombres : ")
apellidos = input("Ingrese sus apellidos : ")
ubicacion = input("Cual es su ubicacion : ")
direccion = input("Cual es su direccion : ")
ciudad = input("De que ciudad eres : ")
longitud = int(input("Cual es la longitud : "))
latitud = int(input("Cual es la latitud : "))
email = input("Ingrese su correo electronico : ")
edad = int(input("Cual es su edad : "))
ocupacion = input("Cual es su ocupacion : ")


datos = {
            'id' : id,
            'nombres' : nombres,
            'apellidos' : apellidos,
            'ubicacion' : ubicacion,
            'direccion' : direccion,
            'ciudad' : ciudad,
            'longitud' : longitud,
            'latitud' : latitud,
            'email' : email,
            'edad' : edad,  
            'ocupacion': ocupacion
        }

print("Estos son los datos del usuario : ", datos)