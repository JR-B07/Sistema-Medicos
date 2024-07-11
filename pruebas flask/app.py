from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

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
        cursor.execute('SELECT * FROM tbmedicos')
        consultaA = cursor.fetchall()
        return render_template('index.html', albums=consultaA)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla tbmedicos: {e}")
        return render_template('index.html', albums=[])

@app.route('/registros')
def registros():
    return render_template('registros.html')

@app.route('/consulta')
def consulta():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_medicos')
    medicos = cursor.fetchall()
    return render_template('consulta.html', medicos=medicos)

@app.route('/expedientes')
def expedientes():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_pacientes')
        pacientes = cursor.fetchall()
        return render_template('expedientes.html', pacientes=pacientes)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla tb_pacientes: {e}")
        return render_template('expedientes.html', pacientes=[])

@app.route('/guardarPaciente', methods=['POST'])
def guardarPaciente():
    if request.method == 'POST':
        fnombre = request.form['txtnombre']
        fpaciente = request.form['txtpaciente']
        ffecha = request.form['txtfecha']
        
        cursor = mysql.connection.cursor()

        # Verificar si el médico existe en la tabla tb_medicos
        cursor.execute('SELECT * FROM tb_medicos WHERE nombre = %s', (fnombre,))
        medico = cursor.fetchone()

        if medico is None:
            flash('El nombre del médico no existe en la tabla de médicos.')
            return redirect(url_for('expedientes'))

        # Insertar el nuevo paciente
        cursor.execute('INSERT INTO tb_pacientes (nombre, paciente, fecha, id_medico) VALUES (%s, %s, %s, %s)', (fnombre, fpaciente, ffecha, medico[0]))
        mysql.connection.commit()
        flash('Expediente generado correctamente')
        return redirect(url_for('expedientes'))

@app.route('/guardarMedico', methods=['POST'])
def guardarMedico():
    if request.method == 'POST':
        fnombre = request.form['txtnombre']
        fcorreo = request.form['txtcorreo']
        frol = request.form['txtrol']
        fcedula = request.form['txtcedula']
        frfc = request.form['txtrfc']
        fcontrasena = request.form['txtcontrasena']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO tb_medicos (nombre, correo, id_roles, cedula, rfc, contrasena) VALUES (%s, %s, %s, %s, %s, %s)', (fnombre, fcorreo, frol, fcedula, frfc, fcontrasena))
        mysql.connection.commit()
        flash('Médico integrado correctamente')
        return redirect(url_for('consulta'))

@app.route('/editarPaciente/<int:id>', methods=['GET', 'POST'])
def editarPaciente(id):
    if request.method == 'POST':
        fnombre = request.form['txtnombre']
        fpaciente = request.form['txtpaciente']
        ffecha = request.form['txtfecha']
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE tb_pacientes SET nombre=%s, paciente=%s, fecha=%s WHERE id=%s', (fnombre, fpaciente, ffecha, id))
        mysql.connection.commit()
        flash('Paciente actualizado correctamente')
        return redirect(url_for('expedientes'))
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_pacientes WHERE id=%s', (id,))
        paciente = cursor.fetchone()
        return render_template('editar_paciente.html', paciente=paciente)

@app.route('/eliminarPaciente/<int:id>', methods=['GET', 'POST'])
def eliminarPaciente(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM tb_pacientes WHERE id=%s', (id,))
    mysql.connection.commit()
    flash('Paciente eliminado correctamente')
    return redirect(url_for('expedientes'))

@app.errorhandler(404)
def paginando(e):
    return 'sintaxis incorrecta'

def create_tables():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="bdflask")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_medicos (
            id_medico INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50),
            correo VARCHAR(45),
            id_roles INT,
            cedula VARCHAR(8),
            rfc VARCHAR(11),
            contrasena VARCHAR(45)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_pacientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50),
            paciente VARCHAR(50),
            fecha DATE,
            id_medico INT,
            FOREIGN KEY (id_medico) REFERENCES tb_medicos(id_medico)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=7000)
