from flask import Flask
from conexion_bd import base_de_datos

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/reposteria_flask'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

base_de_datos.init_app(app)


@app.route("/")
def initial_controller():
    return {
        "message": "Bienvenido a mi API de REPOSTERIA 🥧"
    }



if __name__ == '__main__' :
    app.run(debug=True)
