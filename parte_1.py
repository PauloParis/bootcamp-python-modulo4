
from clases import Automovil


insertar = int(input('Cuantos Vehículos desea insertar: '))
vehiculos = [] 

for i in range(insertar):

    print('\nDatos del automóvil ', i)
    marca = input('Inserte la marca del automóvil: ')
    modelo = input('Inserte el modelo: ')
    numRuedas = input('Inserte el número de ruedas: ')
    velocidad = input('Inserte la velocidad en km/h: ')
    cilindraje = input('Inserte el cilindraje en cc: ')

    automovil = Automovil(marca, modelo, numRuedas, velocidad, cilindraje)
    vehiculos.append(automovil)


# Instancias sin el for

""" automovil_1 = Automovil('Toyota', 'Yaris', 4, 120, 800)
automovil_2 = Automovil('Fiat', 'Palio', 4, 95, 1200)
automovil_3 = Automovil('Ford', 'Fiesta', 4, 125, 1500) """



print('\nImprimiendo por pantalla los Vehículos: \n')



for index, vehiculo in enumerate(vehiculos):
    print(f'Datos del automóvil {index+1} :  {vehiculo}')

    