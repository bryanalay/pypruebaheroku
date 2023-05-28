from flask import Flask
import os

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta y una función asociada a esa ruta
@app.route('/')
def hello():
    return "¡Dave ve zoofalia!!! brulrlrlrlrl"

# Obtén el número del puerto asignado por Heroku o utiliza el puerto 5000 de forma predeterminada
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    # Ejecuta la aplicación en el puerto especificado
    app.run(host='0.0.0.0', port=port)
