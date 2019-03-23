from flask import Flask, render_template

from plumerillo.medoymana.persistencia import Usuarios, Necesidades, Habilidades

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/pages/contacto.html/', methods=['GET'])
def contacto():
    return  render_template('pages/contacto.html')

@app.route('/pages/perfil-usuario.html/', methods=['GET'])
def perfilusuario():
    return  render_template('pages/perfil-usuario.html')

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
