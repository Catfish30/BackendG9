from flask import Flask
from conexion_bd import base_de_datos
from models.ingrediente import IngredienteModel
from models.receta import RecetaModel
from models.preparacion import PreparacionModel
from models.recetas_ingredientes import RecetaIngredienteModel
from models.log import LogModel

from controllers.ingrediente import IngredientesController, IngredienteController, FiltroIngredientesController
from flask_restful import Api

from os import environ
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
api = Api(app=app)


app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')  #'mysql://root:root@localhost:3306/reposteria_flask'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

base_de_datos.init_app(app)

# elimina todas las tablas del proyecto
# base_de_datos.drop_all(app=app)


base_de_datos.create_all(app=app)


@app.route("/")
def initial_controller():
    return {
        "message": "Bienvenido a mi API de REPOSTERIA 🥧"
    }


# Zona erutamiento

api.add_resource(IngredientesController,'/ingredientes')
api.add_resource(IngredienteController, '/ingrediente/<int:id>')
api.add_resource(FiltroIngredientesController, '/buscar_ingrediente')


if __name__ == '__main__' :
    app.run(debug=True)
