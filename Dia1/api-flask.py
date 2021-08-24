from flask import Flask, request

app = Flask(__name__)

productos = []

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
        producto = request.get_json()
        productos.append(producto)
        return {
            "message":"Producto creado Exitosamente",
            "content":producto
        }

# <int:id> parametro que puede cambiar 

@app.route("/producto/<int:id>",methods=['GET'])
def gestion_producto(id):
    
    total_productos = len(productos)
    if id < total_productos:
        return {
            "content":productos[id]
        }
    else:
        return {
            "message":"Producto no encontrado",
            "content":None
        }
    return 

if __name__ == "__main__":
    app.run(debug=True,port=8000)