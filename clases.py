
import csv

class Vehiculo:

    def __init__(self, marca, modelo, numRuedas) -> None:
        self._marca = marca
        self._modelo = modelo
        self._numRuedas = numRuedas

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def numRuedas(self):
        return self._numRuedas
    
    @numRuedas.setter
    def numRuedas(self, numRuedas):
        self._numRuedas = numRuedas
    

    def guardar_datos_csv(documento, *vehiculos):
        try:
            with open(documento, 'w', newline='') as archivo:
                datos = [(vehiculo.__class__, vehiculo.__dict__) for vehiculo in vehiculos]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print('No existe el archivo vehiculos.csv')
        except Exception as e:
            print(e)
    

    def leer_datos_csv(documento):
        try:
            with open(documento, 'r') as archivo:
                archivo_csv = csv.reader(archivo)
                archivo_csv_ordenado = sorted(archivo_csv, key=lambda x: x[0])
                clase = ''
                for item in archivo_csv_ordenado:
                    clase_nombre = item[0].split('.')[-1][:-2]
                    if clase != clase_nombre:
                        clase = clase_nombre
                        print(f'\n\nLista de vehículos {clase}')
                    print(item[1])

        except FileNotFoundError:
            print('No existe el archivo vehiculos.csv')
        except Exception as e:
            print(e)

    def __str__(self) -> str:
        return f'Marca: {self._marca}, Modelo: {self._modelo}, {self._numRuedas} ruedas'
    

class Automovil(Vehiculo):

    def __init__(self, marca, modelo, numRuedas, velocidad, cilindrada) -> None:
        super().__init__(marca, modelo, numRuedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def cilindrada(self):
        return self._cilindrada
    
    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self._cilindrada = cilindrada

    def __str__(self) -> str:
        return f'{super().__str__()}, {self._velocidad} km/h, {self._cilindrada} cc'
    


class Particular(Automovil):

    def __init__(self, marca, modelo, numRuedas, velocidad, cilindrada, numPuestos) -> None:
        super().__init__(marca, modelo, numRuedas, velocidad, cilindrada)
        self._numPuestos = numPuestos

    @property
    def numPuestos(self):
        return self._numPuestos
    
    @numPuestos.setter
    def numPuestos(self, numPuestos):
        self._numPuestos = numPuestos

    def __str__(self) -> str:
        return F'{super().__str__()}, numPuestos: {self._numPuestos}'



class Carga(Automovil):

    def __init__(self, marca, modelo, numRuedas, velocidad, cilindrada, peso) -> None:
        super().__init__(marca, modelo, numRuedas, velocidad, cilindrada)
        self._peso = peso

    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, peso):
        self._peso = peso

    def __str__(self) -> str:
        return f'{super().__str__()}, peso: {self._peso}'



class Bicicleta(Vehiculo):

    def __init__(self, marca, modelo, numRuedas, tipoBicicleta) -> None:
        super().__init__(marca, modelo, numRuedas)
        self._tipoBicicleta = tipoBicicleta

    @property
    def tipoBicicleta(self):
        return self._tipoBicicleta
    
    @tipoBicicleta.setter
    def tipoBicicleta(self, tipoBicicleta):
        self._tipoBicicleta = tipoBicicleta

    def __str__(self) -> str:
        return f'{super().__str__()}, tipoBicicleta: {self._tipoBicicleta}'


class Motocicleta(Bicicleta):

    def __init__(self, marca, modelo, numRuedas, tipoBicicleta, numRadios, cuadro, motor) -> None:
        super().__init__(marca, modelo, numRuedas, tipoBicicleta)
        self._numRadios = numRadios
        self._cuadro = cuadro
        self._motor = motor
    
    @property
    def numRadios(self):
        return self._numRadios
    
    @numRadios.setter
    def numRadios(self, numRadios):
        self._numRadios = numRadios

    @property
    def cuadro(self):
        return self._cuadro
    
    @cuadro.setter
    def cuadro(self, cuadro):
        self._cuadro = cuadro
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor


    def __str__(self) -> str:
        return f'{super().__str__()}, numRadios: {self._numRadios}, cuadro: {self._cuadro}, motor: {self._motor}'