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


def check_habilidades_existe(idUsuario, idHabilidades):
    habilidades = BaseDeDatos.correr_sql(f"SELECT * FROM usuario_habilidad WHERE (ID_usuario = {idUsuario}  and (ID_habilidad = {idHabilidades})")
    return habilidades


def agregar_habilidades(id_usuario, id_habilidad):
    add_Habilidades = BaseDeDatos.correr_sql(f"INSERT INTO usuario_habilidad (id_usuario, id_habilidad) VALUES ({id_usuario},{id_habilidad})")
    return add_Habilidades


def modificar_habilidades(id_usuario, id_habilidad):
    mod_Habilidades = BaseDeDatos.correr_sql(f"ALTER TABLE usuario_habilidad ADD ({id_usuario},{id_habilidad})")
    return mod_Habilidades


def eliminar_habilidades_usuario(id_usuario):
    BaseDeDatos.correr_sql(f"DELETE FROM usuario_habilidad WHERE ID_usuario = {id_usuario}")

