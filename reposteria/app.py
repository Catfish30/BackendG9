from flask import Flask
from conexion_bd import base_de_datos
from models.ingrediente import IngredienteModel
from models.receta import RecetaModel
from models.preparacion import PreparacionModel
from models.recetas_ingredientes import RecetaIngredienteModel

from controllers.ingrediente import IngredientesController
from flask_restful import Api

from os import environ
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
api = Api(app=app)


app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')  #'mysql://root:root@localhost:3306/reposteria_flask'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

base_de_datos.init_app(app)

base_de_datos.create_all(app=app)


@app.route("/")
def initial_controller():
    return {
        "message": "Bienvenido a mi API de REPOSTERIA 🥧"
    }


# Zona erutamiento

api.add_resource(IngredientesController,'/ingredientes')



if __name__ == '__main__' :
    app.run(debug=True)
