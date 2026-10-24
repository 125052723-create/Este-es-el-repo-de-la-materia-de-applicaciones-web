#Importamos paquetes de flask
from flask import Flask, render_template, request

#importacion para generar hash y comprobar si la contra coincide con el hash
from werkzeug.security import generate_password_hash

#Creamos instancia de la app
app = Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'FlaskDB'
app.secret_key = 'mysecretkey'




#RUTA

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/registro", methods=["GET","POST"])
def registro():

    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        correo = request.form["correo"]
        password_hash = request.form["password_hash"]
        id_rol = request.form["id_rol"]


        password_hasheada = generate_password_hash(password_hash)

#Iniciamos servidor Flask en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000)