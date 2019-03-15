from flask import Flask, render_template

from plumerillo.medoymana.persistencia import Usuarios, Necesidades

app = Flask(__name__)


@app.route("/")
def index():
    return app('index.html')

@app.route("/publicaciones/")
def publicacion():
    return render_template('pages/publicaciones.html')


@app.route()

if __name__ == '__main__':
    app.run(debug=True)
