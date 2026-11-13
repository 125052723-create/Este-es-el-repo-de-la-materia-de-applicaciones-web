#Librerias

from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

#Crear applicacion
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

#COnexion a MySQl

app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_albums'
app.secret_key = 'mysecretkey'

mysql = MySQL(app)


#RUTA PRINCIPAL: READ

@app.route('/')
def index():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_albums')
    conAlbums = con.fetchall()
    print(conAlbums)
    return render_template('index.html', listAlbums = conAlbums)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo=request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']
        print(titulo, artista, anio)

        con = mysql.connection.cursor()
        con.execute('INSERT INTO tb_albums(titulo, artista, anio) VALUES(%s, %s, %s)', (titulo, artista, anio))
        mysql.connection.commit()

    flash('El album fue agregado correctamente!')
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_albums WHERE id=%s', (id,))
    consultarID = con.fetchone()
    con.close()
    return render_template('editarAlbum.html', Album=consultarID)

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']

        con = mysql.connection.cursor()
        con.execute('UPDATE tb_albums SET titulo=%s, artista=%s, anio=%s WHERE id=%s', (titulo, artista, anio, id))
        mysql.connection.commit()
    flash('Se actualizo el album ' + titulo)
    return redirect(url_for('index'))


@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar():
    if request.method =='POST':
        titulo = request.form['txtTitulo']

        con = mysql.connection.cursor()
        con.execute('DELETE FROM tb_albums WHERE id=%s', (id,))
        mysql.connection.commit()

    flash('Se elimino el album ' + titulo)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)

