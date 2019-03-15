from plumerillo.medoymana.persistencia import BaseDeDatos


def seleccionar_por_usuario(idUsuario):
    necesidades=BaseDeDatos.correr_sql(f"SELECT * FROM necesidad WHERE ID_USUARIO = {idUsuario}")
    return necesidades



# llamar como seleccionar_por_habilidades(["1", "3", "5"])
def seleccionar_por_habilidades(idHabilidades):
    necesidades=BaseDeDatos.correr_sql(f"SELECT * FROM necesidad WHERE ID_habilidad in ({','.join(idHabilidades)})")
    return necesidades



