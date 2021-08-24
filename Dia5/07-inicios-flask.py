from flask import Flask

# la variable name muestra si el archivo virtual esta llamando a al clase Flask (patron de dise;o Singletton)
app = Flask(__name__)

# print(__name__)

@app.route('/')
def inicio():
    print('Me llamaron')
    return {
        "message*":"Hello World"
    }
    

app.run(debug=True)