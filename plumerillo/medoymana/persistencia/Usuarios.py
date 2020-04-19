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
        usuario['habilidades'] = Habilidades.seleccionar_todos_para_usuario(usuario['id_usuario'])
        return usuario
    else:
        return None


def seleccionar_uno(email, password):
    usuario = BaseDeDatos.correr_sql(f"select * from usuario where email = '{email}' and password = '{password}'")
    if usuario.__len__() == 1:
        usuario = usuario[0]
        return usuario
    else:
        return None


def agregar_usuario(ci, nombre, apellido, fecha_nacimiento, email, telefono, calle, numero_puerta, esquina_1, esquina_2,
                    password):
    usuario = BaseDeDatos.correr_sql(f"INSERT INTO usuario (ci,nombre,apellido,fecha_nacimiento,email,telefono,calle,"
                                     f"numero_puerta,esquina_1,esquina_2,password) VALUES ({ci},'{nombre}',"
                                     f"'{apellido}','{fecha_nacimiento}','{email}',{telefono},'{calle}',"
                                     f"'{numero_puerta}','{esquina_1}','{esquina_2}','{password}')")
    return usuario


