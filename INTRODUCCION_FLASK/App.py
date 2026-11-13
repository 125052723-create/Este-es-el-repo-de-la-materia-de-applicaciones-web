#Importamos los paquetes de flask
from flask import Flask, render_template, request, redirect, url_for,session

#Importar las funciones para generar hashes de la contraseña y comprobar si una contraseña coincide con el hash
from werkzeug.security import generate_password_hash, check_password_hash

from flask_mysqldb import MySQL

#Creamos una instancia de nuestra aplicación
app = Flask(__name__)

#Configuración de la conexión
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MTSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'FlaskDB'
#Permite que Flask vuelva a cargar las plantillas cuando se modifican
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

#Creación de ruta. La ruta / es la ruta raíz, será la que se mostrará cuando el proyecto se ejecute.
@app.route("/")
def home():
    #Estamos retornando una vista HTML de la carpeta de templates
    return render_template("login.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "POST":

        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        correo = request.form["correo"]
        password = request.form["password"]
        id_rol = request.form["id_rol"]

        # Generar el hash de la contraseña
        password_hash = generate_password_hash(password)

        cursor = mysql.connection.cursor()

        # Comprobar si el correo ya existe
        cursor.execute(
            "SELECT id FROM usuarios WHERE correo = %s",
            (correo,)
        )

        if cursor.fetchone():
            cursor.close()
            return render_template(
                "registro.html"
            )

        # Insertar usuario en la base de datos
        cursor.execute("""
            INSERT INTO usuarios
            (nombre, apellido_p, apellido_m, correo, password, id_rol)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nombre,
            apellido_p,
            apellido_m,
            correo,
            password_hash,
            id_rol
        ))

        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("login"))

    return render_template("registro.html")

#Ruta de login
@app.route("/login", methods=["GET", "POST"])
def login():

    #Verificamos si se enviaroon los datos del formulario
    if request.method == "POST":
        #Recuperamos el correo y la contraseña
        correo = request.form["correo"]
        password = request.form["password"]
        #Creamos el cursor para ejercutar la consulta SQL.
        cursor = mysql.connection.cursor()
       
        #Consulta para buscar al usuario por su correo
        sql = """
            SELECT
            usuarios.id,
            usuarios.nombre,
            usuarios.apellido_p,
            usuarios.apellido_m,
            usuarios.correo,
            usuarios.password,
            roles.nombre
            FROM usuarios
            INNER JOIN id_rol
            ON usuarios.id_rol = roles.id_rol
            WHERE usuarios.correo = %s
        """
        #Vamos a ejecutar la consulta pasando como parámetro el correo
        cursor.execute(sql, (correo,))

        usuario = cursor.fetchone()

        cursor.close()
        #Vamos a verificar que la contraseña conincida con el hash generado anteriormente
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
    #Si no hay una session activa lo manda a login
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    #Si el rol es diferente de Administrador, retornará un mensaje
    #de acceso denegado
    if session.get("rol") != "Administrador":
        return "Acceso denegado"
    #Sino mandará a la vista de administrador
    return render_template(
        "administrador.html",
        nombre=session["nombre"])

# PANEL DE USUARIO
@app.route("/usuario")
def usuario():

    if "id_usuario" not in session:
        return redirect(url_for("login"))

    if session.get("rol") != "Usuario":
        return "Acceso denegado", 403

    return render_template(
        "usuarios.html",
        nombre=session["nombre"]
    )


# CERRAR SESIÓN
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


#Iniciamos el servidor FLASK en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000)