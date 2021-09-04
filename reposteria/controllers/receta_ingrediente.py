from flask_restful import Resource, reqparse
from sqlalchemy.sql import base
from models.recetas_ingredientes import RecetaIngredienteModel
from models.receta import RecetaModel
from models.ingrediente import IngredienteModel
from conexion_bd import base_de_datos



class RecetaIngredientesController(Resource):
    serializador = reqparse.RequestParser(bundle_errors=True)
    serializador.add_argument(
        'receta_id',
        type=int,
        required=True,
        location='json',
        help='Falta el id de la receta'
    )
    serializador.add_argument(
        'ingredientes_id',
        type=list,
        required=True,
        location='json',
        help='Falta la lista de ingredientes'
    )
    def post(self):
        data = self.serializador.parse_args()
        print(data)

        receta_id= data['receta_id']
        ingredientes_id = data['ingredientes_id']
        # Buscar si existe la receta segun id
        receta = base_de_datos.session.query(RecetaModel).filter(RecetaModel.recetaId == receta_id).first()

        try:
            if receta is None:
                return{
                    "message":"Receta no existe",
                    "content":None
                },400

            # Iterar esa lista de ingredientes, buscar si existe el ingredientes, agregar el registro en la tabla recetas_ingredientes
            for ingrediente in ingredientes_id:
                ingredientesEncontrado = base_de_datos.session.query(IngredienteModel).filter(IngredienteModel.ingredienteId == ingrediente).first()
                if ingredientesEncontrado is None:
                    raise Exception("Ingrediente incorrecto")

                nueva_receta_ingrediente = RecetaIngredienteModel()
                nueva_receta_ingrediente.ingrediente = ingrediente
                nueva_receta_ingrediente.receta = receta_id
                nueva_receta_ingrediente.recetaIngredienteCantidad = 5
                base_de_datos.session.add(nueva_receta_ingrediente)
            base_de_datos.session.commit()
            return{
                "message":"Agregado exitosamente"
            },201
        except Exception as err:
            base_de_datos.session.rollback()
            # Agregar ese error a los Logs
            return{
                "message":err.args[0],
                "content":None
            },400