USE mdm3;
/*Correr luego de la creación de usuarios*/
ALTER TABLE usuario
    ADD password VARCHAR(255) DEFAULT 'pass123'
