class Vehiculo:
    ruedas = 4
    color = 'azul'

vehiculo1 = Vehiculo()
vehiculo1.ruedas = 5
vehiculo1.procedencia = 'Japon'

vehiculo2 = Vehiculo()

print(vehiculo1.ruedas)
print(vehiculo2.ruedas)
print(vehiculo1.procedencia)


class VehiculoConContructor():
    #en todo metodo de la clase SIEMPRE tendremos que colocar como primer parametro la palabra self
    #self: sirve para referenciar a la instancia actual de la clase esto se podria coprara con el uso de this

    def __init__(self, ruedas, color):
        self.ruedas = ruedas
        self.color = color

    def __str__(self):
        return 'Esta es una instancia de la clase VehiculoConConstructor'

vehiculo3 = VehiculoConContructor(4, 'morado')        
print (vehiculo3)




