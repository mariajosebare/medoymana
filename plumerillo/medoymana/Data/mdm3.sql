CREATE DATABASE mdm3;
USE mdm3;
/* se crea la tabla habilidad la que cuenta con un id y el nombre de dicha habilidad*/
CREATE TABLE habilidad (
	id_habilidad INT AUTO_INCREMENT PRIMARY KEY ,
	nombre VARCHAR (50) 
); 

/* se crea la tabla Zona que refiere al area en la que el usuario puede realizar su habilidad dicha tabla cuenta 
con un ID, el departamento del pais en que se encuentra dicho usuario,la cuidad y barrio en que esta. */
CREATE TABLE zona (
	id_zona INT AUTO_INCREMENT PRIMARY KEY,
    departamento VARCHAR(50),
    ciudad VARCHAR (50),
    barrio VARCHAR (50)
);

/* se realiza la tabla usuario la cual cuenta con un ID unico para cada usuario, el documento de identidad (sera información privada
pero a la vez necesaria para la autenticacion y seguridad del usuario),tendra nombre y apellido,correo electronico,telefono,su dirección, y estara 
la tabla conectada con zona.

Los índices de las tablas ayudan a indexar el contenido de diversas columnas para facilitar la búsquedas de contenido de cuando se ejecutan consultas sobre esas tablas.
De ahí que la creación de índices optimiza el rendiemiento de las consultas y a su vez el de la BBDD.*/
CREATE TABLE usuario (
	id_usuario INT AUTO_INCREMENT PRIMARY KEY ,
	ci INT(20),
    nombre VARCHAR (50),
    apellido VARCHAR(50),
    email VARCHAR(50),
    telefono INT (20),
    fecha_nacimiento DATE,
    calle VARCHAR (100),
    numero_puerta VARCHAR (20),
    esquina_1 VARCHAR (50),
    esquina_2 VARCHAR (50),
    id_zona INT,
    INDEX ix_usuario_zona (ID_zona),
    FOREIGN KEY (id_zona) REFERENCES zona (id_zona)
    );

/* se realiza la tabla necesidad la cual se conecta mediante claves foraneas con la tabla habilidad y la tabla del usuario
Una CLAVE FORANEA (FOREING KEY)es una clave que se utiliza para vincular dos tablas.
Una CLAVE FORANEA es un campo (o colección de campos) en una tabla que se refiere a la CLAVE PRIMARIA en otra tabla.
La tabla que contiene la clave externa se denomina tabla secundaria y la tabla que contiene la clave candidata se denomina tabla de referencia o principal.
*/
CREATE TABLE necesidad (
	id_necesidad INT  AUTO_INCREMENT PRIMARY KEY,
    id_habilidad INT,
    id_usuario INT,
    descripcion_necesidad TEXT,
    fecha_creado date,
    INDEX ix_necesidad_habilidad (id_habilidad),
    INDEX ix_necesidad_usuario (id_usuario),
    FOREIGN KEY (id_habilidad) REFERENCES habilidad (id_habilidad),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
      
);

/* se realiza la tabla propuesta la cual esta vinculada a las necesidades que presetan los 2 usuarios en la que la necesidad
de uno de ellos es la habilidad del otro y veceversa.*/ 
CREATE TABLE propuesta (
	id_propuesta INT AUTO_INCREMENT PRIMARY KEY,
	id_necesidad_1 INT,
    id_necesidad_2 INT,
    INDEX ix_propuesta_necesidad_1 (id_necesidad_1),
    INDEX ix_propuesta_necesidad_2 (id_necesidad_2),
    FOREIGN KEY (id_necesidad_1) REFERENCES necesidad (id_necesidad),
    FOREIGN KEY (id_necesidad_2) REFERENCES necesidad (id_necesidad)
    );

/*se realizara una tabla compuesta para unir al usuario y las habilidades*/
CREATE TABLE usuario_habilidad (
	id_usuario_habilidad INT,
	id_usuario INT,
	id_habilidad INT,
    PRIMARY KEY (id_usuario,id_habilidad)
    );

 /* se realiza la tabla del chat.*/ 
CREATE TABLE chat (
	id_chat INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario_1 INT,
	id_usuario_2 INT,
    mensaje VARCHAR(300),
    fecha_hora_mensaje TIMESTAMP,
    FOREIGN KEY (id_usuario_1) REFERENCES usuario (id_usuario),
    FOREIGN KEY (id_usuario_2) REFERENCES usuario (id_usuario)
    );   
	