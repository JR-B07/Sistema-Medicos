import MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL
<< << << < HEAD
== == == =
>>>>>> > d575e17aaa38bb46feecd9556f0721af9973abde

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'
app.secret_key = 'mysecretkey'

<< << << < HEAD
mysql = MySQL(app)

== == == =
app.secret_key = 'mysecretkey'

mysql = MySQL(app)
>>>>>> > d575e17aaa38bb46feecd9556f0721af9973abde


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/home')
def home():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_medicos')
        consultaA = cursor.fetchall()
        return render_template('index.html', albums=consultaA)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla tb_medicos: {e}")
        flash('Error al realizar la consulta.')
        return render_template('index.html', albums=[])


@app.route('/registros')
def registros():
    return render_template('registros.html')


@app.route('/consulta')
def consulta():


<< << << < HEAD
   try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_medicos')
        medicos = cursor.fetchall()
        print(medicos)
        return render_template('consulta.html', medicos=medicos)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla tb_medicos: {e}")
        flash('Error al realizar la consulta.')
        return render_template('consulta.html', medicos=[])

== =====
   cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_medicos')
    medicos = cursor.fetchall()
    return render_template('consulta.html', medicos=medicos)
>>>>>> > d575e17aaa38bb46feecd9556f0721af9973abde


@app.route('/expedientes')
def expedientes():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('''
            SELECT p.id_paciente, p.nombre, p.paciente, p.fecha, m.nombre as nombre_medico
            FROM tb_pacientes p
            JOIN tb_medicos m ON p.id_medico = m.id_medico
        ''')
        pacientes = cursor.fetchall()
        print(pacientes)
        return render_template('expedientes.html', pacientes=pacientes)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla tb_pacientes: {e}")
        flash('Error al realizar la consulta.')
        return render_template('expedientes.html', pacientes=[])


@app.route('/guardarPaciente', methods=['POST'])
def guardarPaciente():
    if request.method == 'POST':
        fnombre = request.form['txtnombre']
        fpaciente = request.form['txtpaciente']
        ffecha = request.form['txtfecha']

        cursor = mysql.connection.cursor()

        cursor.execute(
            'SELECT id_medico FROM tb_medicos WHERE nombre = %s', (fnombre,))
        medico = cursor.fetchone()

        if medico is None:
            flash('El nombre del médico no existe en la tabla de médicos.')
            return redirect(url_for('expedientes'))

<<<<<< < HEAD
   id_medico = medico[0]

    try:
        cursor.execute('INSERT INTO tb_pacientes (nombre, paciente, fecha, id_medico) VALUES (%s, %s, %s, %s)',
                       (fnombre, fpaciente, ffecha, id_medico))
        mysql.connection.commit()
        flash('Expediente generado correctamente')
    except Exception as e:
        print(f"Error al guardar el expediente: {e}")
        flash('Error al generar el expediente. Intente nuevamente.')

    return redirect(url_for('expedientes'))


== =====
   # Insertar el nuevo paciente
   cursor.execute('INSERT INTO tb_pacientes (nombre, paciente, fecha, id_medico) VALUES (%s, %s, %s, %s)', (fnombre, fpaciente, ffecha, medico[0]))
    mysql.connection.commit()
    flash('Expediente generado correctamente')
    return redirect(url_for('expedientes'))

>>>>>> > d575e17aaa38bb46feecd9556f0721af9973abde


@app.route('/guardarMedico', methods=['POST'])
def guardarMedico():
    if request.method == 'POST':
        fnombre = request.form['txtnombre']
        fcorreo = request.form['txtcorreo']
        frol = request.form['txtrol']
        fcedula = request.form['txtcedula']
        frfc = request.form['txtrfc']
<<<<<< < HEAD
   fcontraseña = request.form['txtcontraseña']

    hashed_password = generate_password_hash(fcontraseña, method='sha256')

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO tb_medicos (nombre, correo, id_roles, cedula, rfc, contraseña) VALUES (%s, %s, %s, %s, %s, %s)',
                   (fnombre, fcorreo, frol, fcedula, frfc, hashed_password))
== =====
   fcontrasena = request.form['txtcontrasena']
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO tb_medicos (nombre, correo, id_roles, cedula, rfc, contrasena) VALUES (%s, %s, %s, %s, %s, %s)',
                   (fnombre, fcorreo, frol, fcedula, frfc, fcontrasena))
>>>>>> > d575e17aaa38bb46feecd9556f0721af9973abde
   mysql.connection.commit()
    flash('Médico integrado correctamente')
    return redirect(url_for('consulta'))

<<<<<< < HEAD

== =====
>>>>>> > d575e17aaa38bb46feecd9556f0721af9973abde


@app.route('/editarPaciente/<int:id>', methods=['GET', 'POST'])
def editarPaciente(id):
    if request.method == 'POST':
        fnombre = request.form['txtnombre']
        fpaciente = request.form['txtpaciente']
        ffecha = request.form['txtfecha']
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE tb_pacientes SET nombre=%s, paciente=%s, fecha=%s WHERE id=%s',
                       (fnombre, fpaciente, ffecha, id))
        mysql.connection.commit()
        flash('Paciente actualizado correctamente')
        return redirect(url_for('expedientes'))
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_pacientes WHERE id=%s', (id,))
        paciente = cursor.fetchone()
        return render_template('editar_paciente.html', paciente=paciente)
<<<<<< < HEAD

== =====
>>>>>> > d575e17aaa38bb46feecd9556f0721af9973abde


@app.route('/eliminarPaciente/<int:id>', methods=['GET', 'POST'])
def eliminarPaciente(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM tb_pacientes WHERE id=%s', (id,))
    mysql.connection.commit()
    flash('Paciente eliminado correctamente')
    return redirect(url_for('expedientes'))

<<<<<< < HEAD


@app.errorhandler(404)
def paginando(e):
    return 'Sintaxis incorrecta', 404


if __name__ == '__main__':
    app.run(debug=True, port=3000)
== =====


@app.errorhandler(404)
def paginando(e):
    return 'sintaxis incorrecta'

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=7000)
>>>>>> > d575e17aaa38bb46feecd9556f0721af9973abde
