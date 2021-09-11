from models.Usuario import UsuarioModel
from bcrypt import checkpw
from .conexion_bd import base_de_datos

class Usuario:
    def __init__(self,id,username) :
        self.id = id
        self.username = username
    def __str__(self) :
        return "Usuario con el id='%s' y username= '%s'"%(self.id, self.username)
        # return "Usuario con el id='{}' y username= '{}'".format(self.id, self.username)

def autenticador(username,password):
    '''Funcion encargada en JWT de validar las credenciales, valida si son ingresadas correctamente y luego valida si es el usuario'''
    if username and password:
        usuario = base_de_datos.session.query(UsuarioModel).filter(UsuarioModel.usuarioCorreo == username).first()
        if usuario:
            hash = bytes(usuario.usuarioPassword, 'utf-8')
            pwsBytes = bytes(password, 'utf-8')
            if checkpw(pwsBytes,hash) is True:
                print('Es el usuario')
                return Usuario(usuario.usuarioId, usuario.usuarioCorreo)
    return None

def identificador(payload):
    
    print(payload)
    usuarioId = payload.get('identity')
    usuarioEncontrado = base_de_datos.session.query(UsuarioModel).filter(UsuarioModel.usuarioId == usuarioId).first()
    if usuarioEncontrado:
        return usuarioEncontrado.__dict__
    return None