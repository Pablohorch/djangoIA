from configparser import ConfigParser

import pymysql
import configparser

#metodo para obtener los usuarios
def get_users():
    cnx, cursor = configSQL()

    # ejecuta la consulta SELECT
    cursor.execute('SELECT * FROM users')

    # obtiene los resultados
    results = cursor.fetchall()

    # cierra la conexión
    cnx.close()

    # devuelve los resultados
    return results


#metodo para obtener un usuario y contraseña
def get_user(username, password):
    cnx, cursor = configSQL()

    # ejecuta la consulta SELECT
    cursor.execute('SELECT * FROM users WHERE nombre = %s AND contrasenia = %s', (username, password))

    # obtiene los resultados
    results = cursor.fetchall()

    # cierra la conexión
    cnx.close()

    # devuelve los resultados
    return results



def save_habito(idUser,habitodto):
    cnx, cursor = configSQL()

    # ejecuta la consulta INSERT
    cursor.execute('INSERT INTO '
                   'habitos (idusuario,habito, accion, media_actual, unidad_registro, unidad_media, unidad_revision, proceso) '
                   'VALUES (%s,%s, %s, %s, %s, %s, %s, %s)',
                   (idUser,habitodto.habito, habitodto.accion, habitodto.mediaActual, habitodto.unidadRegistro, habitodto.unidadMedia, habitodto.unidadRevision, habitodto.proceso))

    # guarda los cambios
    cnx.commit()

    # cierra la conexión
    cnx.close()

    # devuelve los resultados
    return True

def get_habitos(idUser):
    cnx, cursor = configSQL()

    # ejecuta la consulta SELECT
    cursor.execute('SELECT * FROM habitos WHERE idusuario = %s', (idUser))

    # obtiene los resultados
    results = cursor.fetchall()

    # cierra la conexión
    cnx.close()

    return results

def configSQL():
    # lee la configuración del archivo config.ini
    config: ConfigParser = configparser.ConfigParser()
    config.read('djangoProject/config.ini')
    # obtiene la configuración de la sección 'mysql'
    mysql_config = config['mysql']
    # conecta a la base de datos utilizando la configuración
    cnx = pymysql.connect(**mysql_config)
    # crea un cursor
    cursor = cnx.cursor()
    return cnx, cursor


