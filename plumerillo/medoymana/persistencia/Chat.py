from plumerillo.medoymana.persistencia import BaseDeDatos, Usuarios


def obtener_mensajes(id1,id2):
    mensajes = BaseDeDatos.correr_sql(f"SELECT * FROM chat WHERE (id_usuario_1 = {id1} or id_usuario_1 = {id2}) and (id_usuario_2 = {id1} or id_usuario_2 = {id2}) order by fecha_hora_mensaje")
    return mensajes


def agregar_mensajes(id1,id2, mensaje):
    mensajes=BaseDeDatos.correr_sql(f"INSERT INTO chat (id_usuario_1,id_usuario_2,mensaje,fecha_hora_mensaje) VALUES ({id1},{id2},'{mensaje}',CURRENT_TIMESTAMP())")
    return True