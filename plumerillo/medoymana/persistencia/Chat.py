from plumerillo.medoymana.persistencia import BaseDeDatos, Usuarios

def obtener_mensajes(id1,id2):
    mensajes = BaseDeDatos.correr_sql(f"SELECT * FROM chat WHERE (ID_usuario_1 = {id1} or ID_usuario_1 = {id2}) and (ID_usuario_2 = {id1} or ID_usuario_2 = {id2}) order by fecha_hora_mensaje")
    return mensajes


def agregar_mensajes(id1,id2, mensaje):
    mensajes=BaseDeDatos.correr_sql(f"INSERT INTO chat (ID_usuario_1,ID_usuario_2,mensaje,fecha_hora_mensaje) VALUES ({id1},{id2},'{mensaje}',CURRENT_TIMESTAMP())")
    return True