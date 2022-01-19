from flask import Flask, request
#request ---> nos da toda la informacion del cliente
from flask_cors import CORS

app = Flask(__name__)
# si solamente le pasamos la aplicacion o la instacvion de flask habilitara los cors para todos los domiions  para todos los metods

CORS(app=app)
#el endPoint
@app.route('/', methods=['POST'])
def inicio():
    # cuando retornamos una respuesta puede contener hasta dos parametros 
    # en el cual el primero sera la data enviada y el segundo sera el estado HTTP.
    print(request.method)
    if request.method == 'POST':
        #Data sensible se envia por el BODY
        #request.get_json() ---> Captura el json enviado por el cliente 
        # y lo convierte automaticamente a un diccionario para que python lo pueda entender
        print(request.get_json())
        data = request.get_json()

        #get(llave) ---> sirve para extraer la informacion de un diccionario 
        # segun su llave y si no existe esa llave entonces retornara VACIO o NULL. 
        # ADICIONAL: como segundo parametro se puede indicar el valor si es que no existe
        if(data.get('nombre')):
            #nombre = data['nombre'] <-- una forma
            nombre = data.get('nombre') #<-- otra forma
            return 'Hola {}!'.format(nombre)
        else:            
            return 'Necesito la informacion',400
    elif request.method == 'GET':                
        return 'Bienvenido a mi API de Productos' , 200

mis_productos = [
    {
        "nombre": "Paneton",
        "precio" : 17.50,
        "disponible": True,
        "fecha_vencimiento" : "2022-01-14" 
    },
    {
        "nombre": "Chocolate",
        "precio" : 6.9,
        "disponible": False,
        "fecha_vencimiento" : "2021-12-30" 
    }    
]

@app.route('/productos', methods=['GET','POST'])
def productos():
    if request.method == 'GET':
        return {
            'data': mis_productos,
            'message': 'Los productos son:',
            'ok': True
        }
    elif request.method == 'POST':
        data = request.get_json()
        mis_productos.append(data) #insertando un registr en una db
        return{
            'data': data,
            'message': 'Producto agregado existosamente',
            'ok':True
        },201
    
# al nostros ponerle el tipo de dato que podemos aceptar y si al momento de enviar 
# no es ese tipo de dato entonces se rechazara autoamticamente la peticion con un estado 404 NOT FOUND
@app.route('/producto/<int:id>', methods = ['GET','PUT'])
def producto(id):
    if request.method == 'GET':
        #Solucion : Sacar la longitud de la lista y validar 
        # si la posicion desesada es MENOR que la lognitud si es MAYOR entonces no existe len(lista)

        #TAREA:
        #recibir el ID que vendria a ser LA POSCION DE LA LISTA (recordemos que empieza en CERO) 
        # y dar el producto a buscar, SI NO EXISTE el producto entonces emitir un message que diga 
        # que el prodcuto no existe
        # {
        #     'data': null,
        #     'message': 'El producto no existe',
        #     'ok' : False
        # }
        if(id < len(mis_productos)):
            return{
                'data': mis_productos[id],
                'message': 'El producto es:',
                'ok' : True
            }
        else:
            return {
            'data': None,
            'message': 'El producto no existe',
            'ok' : False
        }
    elif request.method == 'PUT':
        data = request.get_json()
        if(id < len(mis_productos)):
            mis_productos[id] = data
            return {
                'ok' : True,
                'data': mis_productos[id],
                'message': 'Producto actualizado satisfactoriamente.'
            }, 201
        else:
            return{
                'ok' : False,
                'data': None,
                'message': 'El Producto con el id {} no existe'.format(id)
            }




if __name__ == '__main__':
    app.run(debug=True)

