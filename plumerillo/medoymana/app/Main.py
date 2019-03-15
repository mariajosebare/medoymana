from flask import Flask

from plumerillo.medoymana.persistencia import Usuarios, Necesidades

app = Flask(__name__)


@app.route("/")
def hello():
    Usuarios.seleccionar_match(4, 13)
    #Necesidad = BaseDeDatos.correr_sql(f"SELECT * FROM propuesta WHERE ID_propuesta = ID_propuesta")
    return Necesidades.seleccionar_por_habilidades(["12","13","22"])


if __name__ == '__main__':
    app.run(debug=True)
