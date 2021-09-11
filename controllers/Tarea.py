from config.conexion_bd import base_de_datos
from models.Tarea import TareaModel
from flask_restful import Resource, reqparse
from flask_jwt import current_identity, jwt_required

class TareasController(Resource):

    serializador = reqparse.RequestParser(bundle_errors=True) #bundle_errors agrupa los errores
    serializador.add_argument(
        'titulo',
        type=str,
        location='json',
        required=True,
        help='Falta el titulo'
    )
    serializador.add_argument(
        'descripcion',
        type=str,
        location='json',
        required=True,
        help='Falta la descripcion'
    )
    serializador.add_argument(
        'tags',
        type=list,
        location='json',
        required=True,
        help='Falta los tags'
    )
    serializador.add_argument(
        'estado',
        type=str,
        location='json',
        required=True,
        help='Falta el estado',
        choices=['POR_HACER','HACIENDO','FINALIZADO']
    )

    @jwt_required()
    def post(self):
        data = self.serializador.parse_args()
        
        try:
            nuevaTarea = TareaModel()
            nuevaTarea.tareaTitulo = data.get('titulo')
            nuevaTarea.tareaDescripcion = data.get('descripcion')
            nuevaTarea.tareaEstado = data.get('estado')
            nuevaTarea.tareaTags = data.get('tags')
            nuevaTarea.usuario = current_identity.get('usuarioId')
            # print(current_identity)

            base_de_datos.session.add(nuevaTarea)
            base_de_datos.session.commit()

            return{
                "message": "Tarea creada exitosamente",
                "content": {
                    "tareaId": nuevaTarea.tareaId,
                    "tareaDescripcion": nuevaTarea.tareaDescripcion,
                    "tareaEstado": nuevaTarea.tareaEstado.value,
                    "tareaTags": nuevaTarea.tareaTags,
                    "tareaTitulo": nuevaTarea.tareaTitulo,
                    "tareaFechaCreacion": str(nuevaTarea.tareaFechaCreacion),
                    "usuario": nuevaTarea.usuario
                }
            }
        except Exception as e:

            base_de_datos.session.rollback()
            return{
                "message": "Error al crear la tarea",
                "content":e.args
            }

    @jwt_required()
    def get(self):
        idUsuario = current_identity.get('usuarioId')
        tareasEncontradas = base_de_datos.session.query(TareaModel).filter(TareaModel.usuario == idUsuario ).all()
        # print(tareasEncontradas)

        resultado = []
        for tarea in tareasEncontradas:
            tareaDict = tarea.__dict__.copy()
            del tareaDict['_sa_instance_state']
            tareaDict['tareaFechaCreacion'] = str(tareaDict['tareaFechaCreacion'])
            tareaDict['tareaEstado'] = tareaDict['tareaEstado'].value
            resultado.append(tareaDict)

        return{
            "message":resultado
        }