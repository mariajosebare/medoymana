from plumerillo.medoymana.persistencia import BaseDeDatos


def seleccionar_todos():
    return BaseDeDatos.correr_sql("select * from habilidad")


def seleccionar_todos_para_usuario(idUsuario):
    return BaseDeDatos.correr_sql(f"SELECT * FROM habilidad WHERE id_habilidad IN (SELECT id_habilidad FROM usuario_habilidad WHERE id_usuario = {idUsuario})")


def seleccionar_uno(id):
    habilidad = BaseDeDatos.correr_sql(f"SELECT * FROM habilidad WHERE id_habilidad = {id}")
    if habilidad.__len__() == 1:
        return habilidad[0]
    else:
        return None

