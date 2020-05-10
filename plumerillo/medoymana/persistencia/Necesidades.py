from plumerillo.medoymana.persistencia import BaseDeDatos, Usuarios, Habilidades


def seleccionar_por_usuario(idUsuario):
    necesidades=BaseDeDatos.correr_sql(f"SELECT * FROM necesidad WHERE id_usuario = {idUsuario}")
    return necesidades


# llamar como seleccionar_por_habilidades(["1", "3", "5"])
# idUsuario es el usuario que pide las necesidades, por lo tanto no se debería traer las necesidades del mismo
def seleccionar_por_habilidades(idHabilidades, idUsuario):
    necesidades=BaseDeDatos.correr_sql(f"SELECT * FROM necesidad WHERE ID_habilidad in ({','.join(idHabilidades)}) AND NOT ID_usuario = {idUsuario}")
    for necesidad in necesidades:
        necesidad['usuario'] = Usuarios.seleccionar_por_id(necesidad['ID_usuario'])
    return necesidades


def seleccionar_por_id(idNecesidad):
    necesidad=BaseDeDatos.correr_sql(f"SELECT * FROM necesidad WHERE ID_Necesidad = {idNecesidad}")
    if necesidad.__len__() == 1:
        necesidad = necesidad[0]
        necesidad['habilidad'] = Habilidades.seleccionar_uno(necesidad['ID_habilidad'])
        return necesidad
    else:
        return None


def seleccionar_match(idUsuario, idHabilidad): #id usuario soy yo. idHabilidad es la que yo necesito
    necesidades_match = {}
    retorno = []
    mis_habilidades=[]
    yo = Usuarios.seleccionar_por_id(idUsuario)
    for habilidad in yo['habilidades']:
        mis_habilidades.append(str(habilidad['ID_habilidad']))

    necesidades = seleccionar_por_habilidades(mis_habilidades, idUsuario)
    #Hay que sacar de uno mismo

    for necesidad in necesidades:
        idNecesidad = necesidad['ID_necesidad']
        if idNecesidad not in necesidades_match:
            usuario = Usuarios.seleccionar_por_id(necesidad['ID_usuario'])
            for habilidad in usuario['habilidades']:
                if habilidad['ID_habilidad'] == idHabilidad:
                    necesidades_match[idNecesidad] = necesidad
                    retorno.append(necesidad)
                    break

    return retorno


def obtener_necesidades(idUsuario,idHabilidades):
    necesidades = BaseDeDatos.correr_sql(f"SELECT * FROM necesidad WHERE (ID_habilidad = {idHabilidades} or(ID_usuario ={idUsuario}) order by fecha_creado")
    return necesidades


def agregar_necesidades(id_usuario,id_habilidad,necesidad):
    necesidadId = BaseDeDatos.insert_sql(f"INSERT INTO necesidad (ID_habilidad,ID_usuario,descripcion_necesidad,fecha_creado) VALUES ({id_habilidad},{id_usuario},'{necesidad}',now())")
    return seleccionar_por_id(necesidadId)


