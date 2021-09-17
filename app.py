from flask import Flask, current_app, render_template, request, send_file
from flask_restful import Api
from config.conexion_bd import base_de_datos
# from models.Tarea import TareaModel
from models.Usuario import UsuarioModel
from controllers.Usuario import RegistroController, LoginController,UsuarioController, ResetearPasswordController
from controllers.Tarea import TareasController
from flask_jwt import JWT
from config.seguridad import autenticador,identificador
from dotenv import load_dotenv
from datetime import timedelta, datetime
from os import environ, path, remove
from config.configuracion_jwt import manejo_error_JWT
from cryptography.fernet import Fernet
from json import loads
from bcrypt import hashpw, gensalt
from utils.patrones import PATRON_PASSWORD
from re import search
from uuid import uuid4
from cloudinary import config
from cloudinary.uploader import upload, destroy

load_dotenv()

app = Flask(__name__)
api = Api(app)

config( 
  cloud_name = environ.get('CLOUD_NAME'), 
  api_key = environ.get('API_KEY'), 
  api_secret = environ.get('API_SECRET') 
)

# config son varaibles de configuracion del pryecto de flask
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = environ.get('JWT_SECRET')
app.config['JWT_EXPIRATION_DELTA'] = timedelta(minutes=30)
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
# cambia la ruta de auth a login
app.config['JWT_AUTH_URL_RULE'] = '/login'
# cambio de prefijo 
app.config['JWT_AUTH_HEADER_PREFIX'] = 'BEARER'


jsonwebtoken = JWT(app=app,authentication_handler= autenticador, identity_handler= identificador)

jsonwebtoken.jwt_error_callback = manejo_error_JWT
base_de_datos.init_app(app)
# base_de_datos.drop_all(app=app)
base_de_datos.create_all(app=app)


@jsonwebtoken.jwt_payload_handler
def definir_payload(identity):
    # print(identity)
    creation = datetime.utcnow()
    expiration = creation + current_app.config.get('JWT_EXPIRATION_DELTA')
    not_before_delta = creation + current_app.config.get('JWT_NOT_BEFORE_DELTA')
    user = {
        "id": identity.id,
        "correo": identity.username
    }
    print(current_app.config) # => app.config
    return{
        "iat":creation,
        "exp":expiration,
        "nbf":not_before_delta,
        "usuario": user
    }

@app.route('/prueba-password',methods=['GET'])
def prueba_ninja():
    productos = ['Pera','Manzana','Sandia','Melon','pollo']
    personas = [{
        "nombre": "Eduardo",
        "sexo": "Masculino"
    }, {
        "nombre": "Renzo",
        "sexo": "Masculino"
    }, {
        "nombre": "Giovana",
        "sexo": "Femenino"
    }, {
        "nombre": "Henry",
        "sexo": "Masculino"
    }]
    masculinos = []
    femeninas = []
    for persona in personas:
        if persona['sexo'] == 'Masculino':
            masculinos.append(persona)
        elif persona['sexo'] == 'Femenino':
            femeninas.append(persona)
    return render_template('pruebas.jinja', nombre='Michael', productos=productos, masculinos=masculinos, femeninas=femeninas)

@app.route('/change-password',methods=['GET','POST'])
def cambiar_password():
    if request.method == 'GET':
        print(request.args)
        token = request.args.get('token')
        fernet = Fernet(environ.get('FERNET_SECRET'))
        try:
            resultado = fernet.decrypt(bytes(token, 'utf-8')).decode('utf-8')
            resultado = loads(resultado)

            fecha_caducidad = datetime.strptime(resultado.get(
                    'fecha_caducidad'), '%Y-%m-%d %H:%M:%S.%f')
            print(fecha_caducidad)
            # print(datetime.utcnow())
            fecha_actual = datetime.utcnow()
            if fecha_actual < fecha_caducidad:
                print('todavia hay tiempo')
                print(resultado)
                return render_template('change_password.jinja', correo=resultado['correo'])
            else:
                print('ya no hay tiempo')
                raise Exception('ya no hay tiempo')
                # return render_template('bad_token.jinja')

            # return render_template('change_password.jinja')
        except:
            return render_template('bad_token.jinja')
    elif request.method == 'POST':
        print(request.get_json())

        email = request.get_json().get('email')
        password = request.get_json().get('password')

        usuario = base_de_datos.session.query(UsuarioModel).filter(UsuarioModel.usuarioCorreo == email).first()
        
        if usuario is None:
            return{
                "message":"Usuario no existe"
            },400

        if search(PATRON_PASSWORD, password) is None:
            return{
                "message":"Password invalido, usar minimo 6 caracteres, usar mayusculas numeros y caracteres especiales"
            },400

        password_bytes = bytes(password,'utf-8')
        nuevaPwd = hashpw(password_bytes,gensalt()).decode('utf-8')

        try:

            base_de_datos.session.query(UsuarioModel).filter(UsuarioModel.usuarioId == usuario.usuarioId).update({'usuarioPassword': nuevaPwd})
            base_de_datos.session.commit()

            return{
                "message":"Se cambio la contrasenia exitosamente"
            }
        except Exception as e:
            print(e)
            return{
                "message": "Hubo un error al actualizar el usuario"
            },400

@app.route('/subir-archivo-servidor',methods=['POST'])
def subir_archivo_servidor():
    archivo = request.files.get('imagen')
    if archivo is None:
        return{
            "message":"Archivo no encontrado"
        },404

    print(archivo.filename)# retornara el nombre del archivo
    print(archivo.mimetype)# retornara el formato(tipo) de archivo

    nombre_inicial = archivo.filename
    extension = nombre_inicial.rsplit('.')[-1]
    nuevo_nombre = str(uuid4())+'.'+extension

    archivo.save(path.join('media',nuevo_nombre))
    return{
        "message":"Archivo subido exitosamente",
        "content":{
            "nombre": nuevo_nombre
        }
    },201

@app.route("/multimedia/<string:nombre>", methods=['GET'])
def devolver_imagen_servidor(nombre):
    try:
        return send_file(path.join('media', nombre))
    except:
        return send_file(path.join('media','not_found.png'))

@app.route('/eliminar-archivo-servidor/<string:nombre>', methods=['DELETE'])
def eliminar_archivo_servidor(nombre):
    try:
        remove(path.join('media',nombre))
    finally:
        return{
            "message":'ok'
        },204


@app.route('/subir-imagen-cloudinary',methods=['POST'])
def subir_imagen_cd():
    imagen = request.files.get('imagen')
    print(imagen)
    resultado = upload(imagen)
    return{
        "message":"Archivo subido exitosamente",
        "content":resultado
    }

@app.route('/eliminar-imagen-cloudinary/<string:id>', methods=['DELETE'])
def eliminar_imagen(id):
    respuesta= destroy(id)
    return{
        "message":"Imagen eliminada exitosamente",
        "content":respuesta
    }

# RUTAS
api.add_resource(RegistroController,'/registro')
# api.add_resource(LoginController,'/login')
api.add_resource(UsuarioController,'/usuario')
api.add_resource(TareasController,'/tareas')
api.add_resource(ResetearPasswordController,'/reset-password')

if __name__ == '__main__':
    app.run(debug=True)

