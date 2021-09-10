from flask_restful import Resource, reqparse
from re import search
from bcrypt import hashpw, gensalt, checkpw
from models.Usuario import UsuarioModel
from config.conexion_bd import base_de_datos

PATRON_CORREO = r'\w+[@]\w+[.]\w{2,3}'
PATRON_PASSWORD = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#&?])[A-Za-z\d@$!%*#&?]{6,}'

class RegistroController(Resource):
    serializador = reqparse.RequestParser(bundle_errors=True)
    serializador.add_argument(
        'nombre',
        type=str,
        location='json',
        required=True,
        help='Falta el nombre'
    )

    serializador.add_argument(
        'apellido',
        type=str,
        location='json',
        required=True,
        help='Falta el apellido'
    )
    
    serializador.add_argument(
        'correo',
        type=str,
        location='json',
        required=True,
        help='Falta el correo'
    )

    serializador.add_argument(
        'password',
        type=str,
        location='json',
        required=True,
        help='Falta el password'
    )

    serializador.add_argument(
        'telefono',
        type=str,
        location='json',
        required=True,
        help='Falta el telefono'
    )

    def post(self):
        data = self.serializador.parse_args()
        # print(data)
        correo = data['correo']
        password = data['password']
        if search(PATRON_CORREO,correo) is None:
            return{
                "message":"Correo no valido"
            },400
        if search(PATRON_PASSWORD,password) is None:
            return{
                "message":"Password invalido, usar minimo 6 caracteres, usar mayusculas numeros y caracteres especiales"
            },400
        try:
            nuevoUsuario = UsuarioModel()
            nuevoUsuario.usuarioCorreo = correo
            nuevoUsuario.usuarioNombre = data.get('nombre')
            nuevoUsuario.usuarioTelefono = data.get('telefono')
            nuevoUsuario.usuarioApellido = data.get('apellido')
            # ENCRIPTACION DE LA CONTRASENIA
            passwordBytes = bytes(password,"utf-8")
            # print(passwordBytes)
            salt = gensalt(rounds=10)
            hashPwd = hashpw(passwordBytes,salt)
            hashPwd = hashPwd.decode('utf-8')
            nuevoUsuario.usuarioPassword = hashPwd
            # Agregando a la base de datos
            base_de_datos.session.add(nuevoUsuario)
            base_de_datos.session.commit()
            return{
                "message":"Usuario creado exitosamente"
            },201
        except Exception as e:
            base_de_datos.session.rollback()
            return{
                "message":"Error al ingresar el usuario",
                "content": e.args
            },500
class LoginController(Resource):
    serializador = reqparse.RequestParser(bundle_errors=True)
    serializador.add_argument(
        'correo',
        type=str,
        location='json',
        required=True,
        help='Falta el correo'
    )
    serializador.add_argument(
        'password',
        type=str,
        location='json',
        required=True,
        help='Falta la password'
    )

    def post(self):
        data = self.serializador.parse_args()
        usuario = base_de_datos.session.query(UsuarioModel).filter(UsuarioModel.usuarioCorreo==data.get('correo')).first()

        if usuario is None:
            return{
                "message": "Usuario no encontrado"
            },404
        password = bytes(data.get('password'),'utf-8')
        usuarioPwd = bytes(usuario.usuarioPassword,'utf-8')
        print(checkpw(password,usuarioPwd))
        return{
            "message":"Usuario encontrado"
        }