#Importamos paquetes de flask
from flask import Flask, render_template, request, redirect, url_for, session

#importacion para generar hash y comprobar si la contra coincide con el hash
from werkzeug.security import generate_password_hash, check_password_hash

from flask_mysqldb import MySQL

#Creamos instancia de la app
app = Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'FlaskDB'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)



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
        password = request.form["password_hash"]
        id_rol = request.form["id_rol"]

        #Vamos a generar un hash apartir de la contraseña
        password_hash = generate_password_hash(password)

        cursor = mysql.connection.cursor()

        cursor.execute(
            "SELECT id FROM usuarios WHERE correo = %s",
            (correo,)
        )

        if cursor.fetchone():
            cursor.close()
            return render_template(
                "registro.html"
            )

        cursor.execute(
            """INSERT INTO usuarios
            (nombre, apellido_p, apellido_m, correo, pawwsord, id_rol)
            VALUES(%s, %s, %s, %s, %s, %s)""",
            (nombre, apellido_p, apellido_m, correo, password_hash, id_rol)
        )

        mysql.connection.commit()
        cursor.close()

        #Con URL_FOR manda a la ruta que tiene por nombre esa funcion
        return redirect(url_for("home"))
    return render_template("registro.html")

#Ruta de login
@app.route("/login", methods=["GET", "POST"])
def login():

    #Verificamos si se enviaron los datos del formulario
    if request.method == "POST":
        #Recuperamos el correo y la contraseña
        correo = request.form["correo"]
        password = request.form["password"]
        #Creamos el cursor para ejecutar la consulta SQL
        cursor = mysql.connection.cursor()
        #Consulta para buscar al usuario por su correo

        sql = """ SELECT usuarios.id, 
        usuarios.nombre, 
        usuarios.apellido_p, 
        usuarios.apellido_m, 
        usuarios.correo, 
        usuarios.password 
        roles.nombre 
        FROM usuarios INNER JOIN id_rol ON usuarios.id_rol = roles.id_rol 
        WHERE usuario.correo = %s"""

        #Vamos a ejecutar la consulta pasando como parametro el correo
        cursor.execute(sql, (correo,))

        usuario = cursor.fetchone()

        cursor.close()

    #Vamos a verificar que la contraseña coincida con el hash generado anteriormente
        if usuario and check_password_hash(usuario[5], password):

            session["id_usuario"] = usuario[0]

            session["nombre"] = usuario[1]

            session["rol"] = usuario[6]

            if session["rol"] == "Administrador":
                return redirect(url_for("admin"))

            return redirect(url_for("usuario"))
        return render_template("login.html")

#Ruta de administrador
@app.route("/admin")
def admin():
    #Si no hay una sesion activa lo manda a login
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    #Si el rol es diferente de Administrador, retomara un mensaje
    #de acceso denegado
    if session.get("rol") != "Administrador":
        return "Accesso denegado"
    #Sino mandara a la vista de administrador
    return render_template("administrador.html", nombre=session["nombre"])

#Iniciamos servidor Flask en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000)