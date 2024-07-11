from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL
<<<<<<< HEAD
=======
from werkzeug.security import generate_password_hash, check_password_hash
>>>>>>> f966823e0ccc8fc82f6ec5c1b672e72be36ec9d3

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
<<<<<<< HEAD
app.config['MYSQL_DB'] = 'tbmedicos'

=======
app.config['MYSQL_DB'] = 'bdflask'
>>>>>>> f966823e0ccc8fc82f6ec5c1b672e72be36ec9d3
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
        cursor.execute('SELECT * FROM tb_medicos')
        consultaA = cursor.fetchall()
        return render_template('index.html', albums=consultaA)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla tb_medicos: {e}")
        flash('Error al realizar la consulta.')
        return render_template('index.html', albums=[])

<<<<<<< HEAD

@app.route('/registro', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        try:
            Fnombre = request.form['txtNombre']
            Frfc = request.form['txtRfc']
            Fcedula = request.form['txtCedula']
            Fcorreo = request.form['txtCorreo']
            Fcontraseña = request.form['txtContraseña']
            Frol = request.form['txtRol']
            
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO tbmedicos (nombre, rfc, cedulaP, correoE, contraseña, rol) VALUES (%s, %s, %s, %s, %s, %s)', 
                           (Fnombre, Frfc, Fcedula, Fcorreo, Fcontraseña, Frol))
            mysql.connection.commit()
            flash('Médico registrado correctamente')
            return redirect(url_for('consultas')) 
        except Exception as e:
            print(f"Error al registrar el médico: {e}")
            flash('Error al registrar el médico: ' + str(e))
            return redirect(url_for('formulario'))  
    
    return render_template('GuardarAlbum.html')
=======

@app.route('/registros')
def registros():
    return render_template('registros.html')


@app.route('/consulta')
def consulta():
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

>>>>>>> f966823e0ccc8fc82f6ec5c1b672e72be36ec9d3

@app.route('/consultas')
def consultas():
    try:
        cursor = mysql.connection.cursor()
<<<<<<< HEAD
        cursor.execute('SELECT * FROM tbmedicos')
        consultaA = cursor.fetchall()
        return render_template('consultaMedicos.html', view='ConsultaMedicos', medicos=consultaA)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla tbmedicos: {e}")
        return render_template('consultaMedicos.html', view='ConsultaMedicos', medicos=[])

@app.route('/editar/<id>')
def editar(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM tbmedicos WHERE id=%s', [id])
        consultaA = cur.fetchone()
        return render_template('editar.html', medicos=consultaA)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla tbmedicos: {e}")
        flash('Error al consultar el médico: ' + str(e))
        return redirect(url_for('home'))

@app.route('/ActualizarAlbum/<id>', methods=['POST'])
def ActualizarAlbum(id):
    if request.method == 'POST':
        try:
            Fnombre = request.form['txtNombre']
            Frfc = request.form['txtRfc']
            Fcedula = request.form['txtCedula']
            Fcorreo = request.form['txtCorreo']
            Fcontraseña = request.form['txtContraseña']
            Frol = request.form['txtRol']

            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE tbmedicos SET nombre=%s, rfc=%s, cedulaP=%s, correoE=%s, contraseña=%s, rol=%s WHERE id=%s',
                           (Fnombre, Frfc, Fcedula, Fcorreo, Fcontraseña, Frol, id))
            mysql.connection.commit()
            flash('Médico actualizado correctamente')
            return redirect(url_for('home'))
=======
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
>>>>>>> f966823e0ccc8fc82f6ec5c1b672e72be36ec9d3

        except Exception as e:
            flash('Error al actualizar el médico: ' + str(e))
            print(e)
            return redirect(url_for('home'))

<<<<<<< HEAD
@app.route('/eliminar/<id>')
def eliminar(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM tbmedicos WHERE id=%s', [id])
        mysql.connection.commit()
        flash('Se ha eliminado correctamente')
        return redirect(url_for('home'))
    except Exception as e:
        flash('Error al eliminar: ' + str(e))
        return redirect(url_for('home'))
    
    
@app.route('/expediente')
def expediente():
    return render_template('expediente.html')

@app.route('/registroP', methods=['GET', 'POST'])
def registroP():
    if request.method == 'POST':
        try:
            Fmedico = request.form['txtMedico']
            Fnombre = request.form['txtNombre']
            Ffecha_nac = request.form['txtfecha_nac']
            Fenfermedades_cronicas = request.form['txtenfermedades_cronicas']
            Falergias = request.form['txtalergias']
            Fantecedentes_familiares = request.form['txtantecedentes_familiares']
            
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO pacientes (medico, nombre, fecha_nac, enfermedades_cronicas, alergias, antecedentes_familiares) VALUES (%s, %s, %s, %s, %s, %s)', 
                           (Fmedico, Fnombre, Ffecha_nac, Fenfermedades_cronicas, Falergias, Fantecedentes_familiares))
            mysql.connection.commit()
            flash('Paciente registrado correctamente')
            return redirect(url_for('expediente')) 
        except Exception as e:
            print(f"Error al registrar al paciente: {e}")
            flash('Error al registrar al paciente: ' + str(e))
            return redirect(url_for('expediente'))  
    
    return render_template('guardarpacientes.html')

@app.route('/exploracion')
def exploracion():
    return render_template('exploracion.html')

@app.route('/diagnostico')
def diagnostico():
    return render_template('diagnostico.html')

@app.route('/consultarPacientes')
def consultaP():
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM pacientes')
            consultaA = cursor.fetchall()
            return render_template('consultaP.html', view='consultaP', pacientes=consultaA)
        except Exception as e:
            print(f"Error al realizar la consulta en la tabla tbmedicos: {e}")
            return render_template('consultaP.html', view='consultaP', pacientes=[])
    
@app.route('/editarP/<id>')
def editarP(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM pacientes WHERE id=%s', [id])
        consultaA = cur.fetchone()
        return render_template('editarP.html', pacientes=consultaA)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla tbmedicos: {e}")
        flash('Error al consultar el médico: ' + str(e))
        return redirect(url_for('expediente'))

@app.route('/ActualizarP/<id>', methods=['POST'])
def ActualizarP(id):
    if request.method == 'POST':
        try:
            Fmedico = request.form['txtMedico']
            Fnombre = request.form['txtNombre']
            Ffecha_nac = request.form['txtfecha_nac']
            Fenfermedades_cronicas = request.form['txtenfermedades_cronicas']
            Falergias = request.form['txtalergias']
            Fantecedentes_familiares = request.form['txtantecedentes_familiares']

            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE pacientes SET medico=%s, nombre=%s, fecha_nac=%s, enfermedades_cronicas=%s, alergias=%s, antecedentes_familiares=%s WHERE id=%s', 
                           (Fmedico, Fnombre, Ffecha_nac, Fenfermedades_cronicas, Falergias, Fantecedentes_familiares, id))
            
            mysql.connection.commit()
            flash('Médico actualizado correctamente')
            return redirect(url_for('expediente'))

        except Exception as e:
            flash('Error al actualizar el médico: ' + str(e))
            print(e)
            return redirect(url_for('expediente'))
=======
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


@app.route('/guardarMedico', methods=['POST'])
def guardarMedico():
    if request.method == 'POST':
        fnombre = request.form['txtnombre']
        fcorreo = request.form['txtcorreo']
        frol = request.form['txtrol']
        fcedula = request.form['txtcedula']
        frfc = request.form['txtrfc']
        fcontraseña = request.form['txtcontraseña']

        hashed_password = generate_password_hash(fcontraseña, method='sha256')

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO tb_medicos (nombre, correo, id_roles, cedula, rfc, contraseña) VALUES (%s, %s, %s, %s, %s, %s)',
                       (fnombre, fcorreo, frol, fcedula, frfc, hashed_password))
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


@app.route('/eliminarPaciente/<int:id>', methods=['GET', 'POST'])
def eliminarPaciente(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM tb_pacientes WHERE id=%s', (id,))
    mysql.connection.commit()
    flash('Paciente eliminado correctamente')
    return redirect(url_for('expedientes'))


@app.errorhandler(404)
def paginando(e):
    return 'Sintaxis incorrecta', 404

>>>>>>> f966823e0ccc8fc82f6ec5c1b672e72be36ec9d3

    
if __name__ == '__main__':
<<<<<<< HEAD
    app.run(port=9000, debug=True)
=======
    app.run(debug=True, port=3000)
>>>>>>> f966823e0ccc8fc82f6ec5c1b672e72be36ec9d3
