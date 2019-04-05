import os
from flask import Flask, render_template, request

from plumerillo.medoymana.persistencia import Usuarios, Necesidades, Habilidades

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


"""
# Revisar el upload img user
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)

    #return render_template('index.html')
# . revisar upload img user"""


@app.route("/publicaciones/<int:id_habilidad>", methods=['GET'])
def publicacion(id_habilidad):
    result = {
        'habilidades': Habilidades.seleccionar_todos(),
        'necesidades': Necesidades.seleccionar_por_usuario(id_habilidad)
    }
    return render_template('pages/publicaciones.html', result=result)

@app.route("/matcheo/<int:id_necesidad>", methods=['GET'])
def matcheo(id_necesidad):
    necesidad = Necesidades.seleccionar_por_id(id_necesidad)
    result = {
        'necesidades': Necesidades.seleccionar_match(necesidad['ID_usuario'], necesidad['ID_habilidad']),
        'publicacion': necesidad
    }
    return render_template('pages/matcheo.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
