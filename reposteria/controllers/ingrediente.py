from flask_restful import Resource, request,reqparse
import sqlalchemy
from models.ingrediente import IngredienteModel
from conexion_bd import base_de_datos
from models.log import LogModel

serializador = reqparse.RequestParser()
serializador.add_argument(
    'nombre',
    required=True,
    location='json',
    help='Falta el nombre',
    type=str,
)

class IngredientesController(Resource):
    def get(self):
        ingredientes = base_de_datos.session.query(IngredienteModel).all()
        print(ingredientes)
        resultado = []
        for ingrediente in ingredientes:
            print(ingrediente)
            print(ingrediente.__dict__)
            ingrediente_dicc = ingrediente.__dict__
            del ingrediente_dicc['_sa_instance_state']
            resultado.append(ingrediente_dicc)
        print("Ingreso al get")
        return {
            "message": None,
            "content": resultado
        }

    def post(self):
        # validar en base a los argumentos indicados si esta cumpliendo o no el front con pasar dicha informacion
        data = serializador.parse_args()
        try:
            nuevoIngrediente = IngredienteModel(
                ingredienteNombre=data['nombre'])
            # inicializando una transaccion
            base_de_datos.session.add(nuevoIngrediente)
            base_de_datos.session.commit()
            # print(nuevoIngrediente.__dict__)
            json = {
                "id": nuevoIngrediente.ingredienteId,
                "nombre": nuevoIngrediente.ingredienteNombre
            }
            error = None
            return {
                "message": "Ingrediente creado exitosamente",
                "content": json
            }, 201
        except sqlalchemy.exc.DataError as err:
            error = err
            return {
                "message": "Error al ingresar el ingrediente"
            }, 500

        except sqlalchemy.exc.IntegrityError as err:
            error = err
            return {
                "message": "Ese ingrediente ya existe"
            }, 500

        except Exception as err:
            error = err
            print(err)
            return {
                "message": "Error Desconocido"
            }, 500

        finally:
            # se va a ejecutar si ingreso o no ingreso a algun except
            print('ingreso al finally')
            if error is not None:
                base_de_datos.session.rollback()
                nuevoLog = LogModel()
                nuevoLog.logRazon = str(error)
                base_de_datos.session.add(nuevoLog)
                base_de_datos.session.commit()


class IngredienteController(Resource):
    def get(self, id):
        resultado1 = base_de_datos.session.query(
            IngredienteModel).filter(IngredienteModel.ingredienteId == id).first()

        resultado2 = base_de_datos.session.query(
            IngredienteModel).filter_by(ingredienteId=id).first()

        print(resultado1)
        print(resultado2)
        return {
            "message": id
        }

    def put(self):
        pass

    def delete(self):
        pass