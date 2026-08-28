# ==========
# Practica 0
# Hola mundo con flask + Jinja
# ==========

from flask import Flask, render_template, request

# Crear la aplicacion Flask
app = Flask(__name__)

# Ruta principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Ruta que recibe el nombre enviado por el formulario
@app.route("/saludar", methods=["POST"])
def saludar():

    # Recuperar el dato cuyo name en HTML es "nombre"
    nombre = request.form["nombre"]
    pasatiempos = request.form.getlist("pasatiempos")
    me_gusta = request.form["me_gusta"]

    # Enviar la variable nombre hacia saludar.html
    return render_template(
        "saludar.html",
        nombre=nombre,
        pasatiempos=pasatiempos,
        me_gusta=me_gusta
    )

# Iniciar el servicor de desarrollo
if __name__ == "__main__":
    app.run(debug=True)