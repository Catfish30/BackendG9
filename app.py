from flask import Flask, current_app, render_template, request
from flask_restful import Api
from config.conexion_bd import base_de_datos
# from models.Tarea import TareaModel
# from models.Usuario import UsuarioModel
from controllers.Usuario import RegistroController, LoginController,UsuarioController, ResetearPasswordController
from controllers.Tarea import TareasController
from flask_jwt import JWT
from config.seguridad import autenticador,identificador
from dotenv import load_dotenv
from datetime import timedelta, datetime
from os import environ
from config.configuracion_jwt import manejo_error_JWT
from cryptography.fernet import Fernet
from json import loads

load_dotenv()

app = Flask(__name__)
api = Api(app)

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
                return render_template('change_password.jinja')
            else:
                print('ya no hay tiempo')
                raise Exception('ya no hay tiempo')
                # return render_template('bad_token.jinja')

            # return render_template('change_password.jinja')
        except:
            return render_template('bad_token.jinja')
    elif request.method == 'POST':
        return{
            "message":"Se cambio la contrasenia exitosamente"
        }

        
# RUTAS
api.add_resource(RegistroController,'/registro')
# api.add_resource(LoginController,'/login')
api.add_resource(UsuarioController,'/usuario')
api.add_resource(TareasController,'/tareas')
api.add_resource(ResetearPasswordController,'/reset-password')

if __name__ == '__main__':
    app.run(debug=True)

