USE mdm3;
/* Creamos la tabla para gestionar las notificaciones de mensaje al usuario */

CREATE TABLE alerta ( 
ID_usuario_1 int,
ID_usuario_2 int,
PRIMARY KEY(ID_usuario_1,ID_usuario_2),
FOREIGN KEY (ID_usuario_1) REFERENCES usuario(ID_usuario),
FOREIGN KEY (ID_usuario_2) REFERENCES usuario(ID_usuario)
);