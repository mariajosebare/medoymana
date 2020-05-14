from plumerillo.medoymana.persistencia import BaseDeDatos, Usuarios


def obtener_mensajes(id1, id2):
    mensajes = BaseDeDatos.correr_sql(f"SELECT * FROM chat WHERE (id_usuario_1 = {id1} or id_usuario_1 = {id2}) and (id_usuario_2 = {id1} or id_usuario_2 = {id2}) order by fecha_hora_mensaje")
    eliminar_alertas(id2,id1)
    return mensajes


def agregar_mensajes(id1, id2, mensaje):
    agregar_alerta(id1, id2)
    BaseDeDatos.correr_sql(f"INSERT INTO chat (id_usuario_1,id_usuario_2,mensaje,fecha_hora_mensaje) VALUES ({id1},{id2},'{mensaje}',CURRENT_TIMESTAMP())")
    return True


def obtener_alertas(id2):
    alertas = BaseDeDatos.correr_sql(f"SELECT a.ID_usuario_1, u.nombre FROM alerta a INNER JOIN usuario u ON a.ID_usuario_1 = u.ID_usuario WHERE ID_usuario_2 = '{id2}'")
    return alertas


def eliminar_alertas(id1, id2):
    BaseDeDatos.correr_sql(f"DELETE FROM alerta WHERE ID_usuario_1 = '{id1}' AND ID_usuario_2 = '{id2}'")
    return True


def agregar_alerta(id1, id2):
    BaseDeDatos.correr_sql(f"INSERT INTO alerta (ID_usuario_1, ID_usuario_2) VALUES('{id1}','{id2}')")
    return True
