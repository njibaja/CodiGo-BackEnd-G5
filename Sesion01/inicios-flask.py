from flask import Flask

#Variables de uso propio de python
#__main__ esta variable srive para indicar si estamos en el archivo princiapl del proyeto

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Bienvenido a mi API'



@app.route('/bienvenido')
def bienvenido():
    return 'Te doy la bienvenida a mi API'

@app.route('/bienvenido/home')
def bienvenido_home():
    return 'Te doy la bienvenida a mi API Home'

#Solo se puede retornar un string, tupla y diccionarios

#para que cada vez que nostros hagamos algun cambuio en  cualquier archivo del proyecto y se reinicie automaticamentes
#entonces deberemos indicar el parametro debug = true
if __name__ == '__main__':
    app.run(debug=True)
