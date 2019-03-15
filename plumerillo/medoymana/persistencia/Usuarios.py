from plumerillo.medoymana.persistencia import BaseDeDatos, Habilidades, Necesidades


def seleccionar_todos():
    return BaseDeDatos.correr_sql("select * from usuario")

def seleccionar_uno(id):
    usuario = BaseDeDatos.correr_sql(f"select * from usuario where id_usuario = {id}")
    if usuario.__len__() == 1:
        usuario = usuario[0]
        #usuario['habilidades'] = []
        #for habilidad in Habilidades.seleccionar_todos_para_usuario(usuario['ID_usuario']):
            #usuario['habilidades'].append(habilidad)
        usuario['habilidades'] = Habilidades.seleccionar_todos_para_usuario(usuario['ID_usuario'])
        return usuario
    else:
        return None


def seleccionar_match(idUsuario, idHabilidad): #id usuario soy yo. idHabilidad es la que yo necesito
    usuarios_match = {}
    mis_habilidades=[]
    yo=seleccionar_uno(idUsuario)
    for habilidad in yo['habilidades']:
        mis_habilidades.append(str(habilidad['ID_habilidad']))

    necesidades = Necesidades.seleccionar_por_habilidades(mis_habilidades)
    #Hay que sacar de uno mismo

    for necesidad in necesidades:
        idUsuarioNecesidad = necesidad['ID_usuario']
        if idUsuarioNecesidad not in usuarios_match:
            usuario=seleccionar_uno(idUsuarioNecesidad)
            for habilidad in usuario['habilidades']:
                if habilidad['ID_habilidad']==idHabilidad:
                    usuarios_match[idUsuarioNecesidad] = usuario
                    break

    return usuarios_match
    # ",".join(lista) = pone una lista de string como un solo string de cosas separadas por coma
    # cargar usuarios aca
    # necesidades = BaseDeDatos.correr_sql ("el sql aca")
    # for necesidad in necesidades:
    #   necesidad['usuario'] = Usuarios.seleccionar_uno(necesidad['ID_Usuario']]



    #usuario = seleccionar_uno(idUsuario)
    #llamar las Necesidades.seleccionar_por_habilidades con mis habilidades
    #recorrer las necesidades, y fijarse si el usuario de la necesidad, necesita de una de mis habilidades
    return usuarios_match