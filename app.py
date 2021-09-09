from flask import Flask
from conexion_bd import base_de_datos
from models.ingrediente import IngredienteModel
from models.receta import RecetaModel
from models.preparacion import PreparacionModel
from models.recetas_ingredientes import RecetaIngredienteModel
from models.log import LogModel


from controllers.ingrediente import IngredientesController, IngredienteController, FiltroIngredientesController
from controllers.preparacion import PreparacionesController
from controllers.receta import RecetasController, RecetaController
from controllers.receta_ingrediente import RecetaIngredientesController
from flask_restful import Api

from os import environ
from dotenv import load_dotenv

from flask_cors import CORS

from flask_swagger_ui import get_swaggerui_blueprint

load_dotenv()

# Configuracion Swager Flask

SWAGGER_URL = "/api/docs"
API_URL="/static/swagger.json"
swagger_blueprint = get_swaggerui_blueprint(
    base_url=SWAGGER_URL,
    api_url=API_URL,
    config={
        'app_name':'Reposteria Flask - Documentacion Swagger'
    }
)

# Finconfiguracion


app = Flask(__name__)

app.register_blueprint(swagger_blueprint)

# origin sirve par aindicar que dominio spueden acceder a la API '*' permite acceder a todos
CORS(app=app, origins='*',methods=['GET','POST','PUT','DELETE'],allow_headers='Content-Type')

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

api.add_resource(RecetasController,'/recetas')
api.add_resource(RecetaController,'/receta/<int:id>')

api.add_resource(RecetaIngredientesController,'/recetas_ingredientes')
api.add_resource(PreparacionesController,'/preparaciones','/preparaciones/<int:id>')

if __name__ == '__main__' :
    app.run(debug=True)
