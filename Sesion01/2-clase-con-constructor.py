class Vehiculo:
    '''Clase que sirve para el uso de los vehiculos'''

    def __init__(self, color, modelo, traccion):
        self.color = color
        self.modelo = modelo
        self.traccion = traccion
        # encapsulado el atributo velocidad para que no peuda ser accedido desde afuera de la clase.
        self.__velocidad = 0

    def acelerar(self):
        '''Metodo que acelera el vehcolo de 20 en 20'''
        self.__velocidad += 20
        return 'La velocidad actual es: {} km/h'.format(self.__velocidad)

    def desacelerar(self):
        '''Desacelera la velocidad del vehiculo'''
        self.__velocidad -= 20
        self.__prueba()
        return self.__velocidad

    def __prueba(self):
        '''Metodo privado de la clase que solo pueder accedido dentro de la misma'''
        print('Esto no deberia pasar!')


vehiculo1 = Vehiculo('azul', 'x3', '4x2')

print(vehiculo1.acelerar())
print(vehiculo1.acelerar())
print(vehiculo1.acelerar())
print(vehiculo1.desacelerar())
