from mailbox import NoSuchMailboxError


class Persona:

    def saludar():
        print('Hola')

    def __init__(self, nombre_de_la_persona, edad_persona, estatura_persona, sexo_persona='NS/NO') :
        self.nombre = nombre_de_la_persona
        self.edad = edad_persona
        self.estatura = estatura_persona
        self.sexo = sexo_persona
