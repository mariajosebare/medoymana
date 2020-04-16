from plumerillo.medoymana.persistencia import BaseDeDatos, Usuarios, Habilidades


def seleccionar_por_usuario(idUsuario):
    necesidades=BaseDeDatos.correr_sql(f"SELECT * FROM necesidad WHERE id_usuario = {idUsuario}")
    return necesidades


# llamar como seleccionar_por_habilidades(["1", "3", "5"])
def seleccionar_por_habilidades(idHabilidades):
    necesidades=BaseDeDatos.correr_sql(f"SELECT * FROM necesidad WHERE id_habilidad in ({','.join(idHabilidades)})")
    for necesidad in necesidades:
        necesidad['usuario'] = Usuarios.seleccionar_uno(necesidad['id_usuario'])
    return necesidades


def seleccionar_por_id(idNecesidad):
    necesidad=BaseDeDatos.correr_sql(f"SELECT * FROM necesidad WHERE id_Necesidad = {idNecesidad}")
    if necesidad.__len__() == 1:
        necesidad = necesidad[0]
        necesidad['habilidad'] = Habilidades.seleccionar_uno(necesidad['id_habilidad'])
        return necesidad
    else:
        return None

def seleccionar_match(idUsuario, idHabilidad): #id usuario soy yo. idHabilidad es la que yo necesito
    necesidades_match = {}
    mis_habilidades=[]
    yo = Usuarios.seleccionar_uno(idUsuario)
    for habilidad in yo['habilidades']:
        mis_habilidades.append(str(habilidad['id_habilidad']))

    necesidades = seleccionar_por_habilidades(mis_habilidades)
    #Hay que sacar de uno mismo

    for necesidad in necesidades:
        idNecesidad = necesidad['id_necesidad']
        if idNecesidad not in necesidades_match:
            usuario = Usuarios.seleccionar_uno(necesidad['id_usuario'])
            for habilidad in usuario['habilidades']:
                if habilidad['id_habilidad'] == idHabilidad:
                    necesidades_match[idNecesidad] = necesidad
                    break

    return necesidades_match.values()
