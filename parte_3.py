
from clases import *

print('\n')


automovil = Automovil("Ford", "Fiesta", 4, 180, 500)
particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
particular2 = Particular("Ford 2", "Fiesta 2", 402, 18002, 50002, 502)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "DobleViga", 21)


Vehiculo.guardar_datos_csv("vehiculos.csv", automovil, particular, carga, bicicleta, motocicleta, particular2)

Vehiculo.leer_datos_csv('vehiculos.csv')


print('\n')

