from flask import Flask, render_template, request, jsonify

from plumerillo.medoymana.persistencia import Usuarios, Necesidades, Habilidades, Chat

app = Flask(__name__)

"""UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER"""


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/contacto', methods=['GET'])
def contacto():
    return  render_template('pages/contacto.html')


@app.route('/perfil', methods=['GET'])
def perfilusuario():
    result = {'habilidades': Habilidades.seleccionar_todos_para_usuario(4)}
    return  render_template('pages/perfil-usuario.html', result=result)


@app.route('/chatusuario', methods=['GET'])
def chatUsuarios():
    return  render_template('pages/chat-usuarios.html')


@app.route("/publicaciones/<int:id_habilidad>", methods=['GET'])
def publicacion(id_habilidad):
    result = {
        'habilidades': Habilidades.seleccionar_todos(),
        'necesidades': Necesidades.seleccionar_por_usuario(id_habilidad)
    }
    return jsonify(result)


@app.route("/matcheo/<int:id_necesidad>", methods=['GET'])
def matcheo(id_necesidad):
    necesidad = Necesidades.seleccionar_por_id(id_necesidad)
    result = {
        'necesidades': Necesidades.seleccionar_match(necesidad['ID_usuario'], necesidad['ID_habilidad']),
        'publicacion': necesidad
    }
    return render_template('pages/matcheo.html', result=result)


@app.route("/login", methods=['GET', 'POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    usuario = Usuarios.seleccionar_uno(email, password)
    if usuario is not None:
        result = {
            'habilidades': Habilidades.seleccionar_todos_para_usuario(usuario['ID_usuario']),
            'usuario': usuario
        }
    else:
        result = {'error': 'Usuario o contraseña inválidos'}
    return jsonify(result)


#Realizamos la creacion de la ruta para la creación de usuario
@app.route("/usuarios", methods=['PUT'])
def crear_usuario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    ci = request.form['ci']
    email = request.form['email']
    password = request.form['password']
    fecha_nacimiento =request.form['fecha de nacimiento']
    calle = request.form['calle']
    numero_puerta =request.form['numero de puerta']
    esquina_1 = request.form['esquina 1']
    esquina_2 = request.form['esquina 2']
    Usuarios.agregar_usuario(ci, nombre, apellido, fecha_nacimiento, email, telefono, calle, numero_puerta, esquina_1, esquina_2, password)
    return jsonify(True)

#Finaliza la ruta de creación de usuario

@app.route("/chat/<id_usuario_1>,<id_usuario_2>", methods=['GET'])
def chat(id_usuario_1, id_usuario_2):
    result = {
        'mensaje': Chat.obtener_mensajes(id1=(), id2=())
    }
    return jsonify(result)


@app.route("/chat/<id_usuario_1>,<id_usuario_2>", methods=['PUT'])
def agregar_mensaje_chat(id_usuario_1, id_usuario_2):
    mensaje = request.form['mensaje']

    return Chat.agregar_mensajes(id_usuario_1, id_usuario_2, mensaje)


@app.route("/necesidades", methods=['GET'])
def necesidades():
    habilidades = Habilidades.seleccionar_todos
    return jsonify(habilidades)


if __name__ == '__main__':
    app.run(debug=True)



