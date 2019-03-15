from plumerillo.medoymana.persistencia import BaseDeDatos


def seleccionar_todos():
    return BaseDeDatos.correr_sql("select * from habilidad")


def seleccionar_todos_para_usuario(idUsuario):
    return BaseDeDatos.correr_sql(f"SELECT * FROM habilidad WHERE ID_habilidad IN (SELECT ID_habilidad FROM usuario_habilidad WHERE ID_usuario = {idUsuario})")




