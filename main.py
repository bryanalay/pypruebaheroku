from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta y una función asociada a esa ruta
@app.route('/')
def hello():
    return "¡Dave ve zoofalia!!! brulrlrlrlrl"

# Ejecuta la aplicación en el servidor web integrado de Flask
if __name__ == '__main__':
    app.run()
