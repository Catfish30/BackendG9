from flask_restful import Resource, request,reqparse
from models.ingrediente import IngredienteModel

serializador = reqparse.RepuestParser()
serializador.add_argument(
    'nombre',
    required=True,
    location='json',
    help='Falta el nombre',
    type=str,
)

class IngredientesController(Resource):
    # def get(self):
    #     print('Ingreso al get')
    #     return {
    #         "message":"Bienvenido al get"
    #     }
    def post(self):
        data = serializador.parse_args()
        nuevoIngrediente = IngredienteModel(ingredienteNombre=data['nombre'])
        print(nuevoIngrediente)
        return {
            "message":"Bienvenido al post"
        }