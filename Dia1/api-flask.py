from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

productos = [
    {"nombre":"Palta",
    "precio":3.5}
]

@app.route("/")
def inicio():
    # siempre que vamos a responder al cliente tiene que ser por el return
    return{
        "message":"Bienvenido a mi API",
        "content":""
    }
# """
# C => POST
# R => GET
# U => PUT | PATCH ID
# D => DELETE
# """

@app.route("/productos",methods=['POST','GET'])
def gestion_productos():

    print(request.method)

    if request.method == 'GET':
        return{
            "message":"",
            "content":productos
        }

    elif request.method == 'POST':
        # get_json sirve para visualizar toda la informacionque el usuario me esta enviando por el body, el body es el cuepro de la peticion (donde el front adjunta la informacion que quiere enviar)
        # body se envia en formato JSON, multipart , TEXT, XML
        producto = request.get_json() #cliente manda json y lo convierte en diccionario, GET_JSON
        productos.append(producto)
        return {
            "message":"Producto creado Exitosamente",
            "content":producto
        }

# <int:id> parametro que puede cambiar 

@app.route("/producto/<int:id>",methods=['GET','PUT','DELETE'])
def gestion_producto(id): #se recibe el id y se tiene que poner en la funcion para usarse tiene que ser el mismo nombre 
   
    total_productos = len(productos)
    if id < total_productos:
        if request.method == 'GET' :
            return {
                "content":productos[id],
                "message":None
            },200
        elif request.method == 'PUT' :
            data = request.get_json()
            productos[id] = data
            return{
                "content":productos[id],
                "message":'Producto actualizado exitosamente'
            },201
        elif request.method == 'DELETE':

            # del productos[id]

            productos.pop(id)
            return{
                "content":None,
                "message":'Producto eliminado'
            }
    else:
        return {
            "message":"Producto no encontrado",
            "content":None
        },404
    return 
#controladores
    
        

if __name__ == "__main__":
    app.run(debug=True,port=8000)