#from asyncio import Task, tasks
#from crypt import methods
#from sqlite3 import Cursor
#from webbrowser import get
from optparse import Values
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config

app=Flask(__name__)

conexion=MySQL(app)

@app.route('/cursos')
def listar_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT nombre, apellido, cc FROM usuario"
        cursor.execute(sql)
        datos=cursor.fetchall()
        cursos = []
        for fila in datos:
            curso = {'nombre': fila[0],'apellido': fila[1],'cc': fila[2]}
            cursos.append(curso)
        return jsonify({'cursos':cursos,'mensaje':"Estos son los cursos Listados!"})
    except Exception as e:
     return "error"
    
@app.route('/cursos/<cc>')
def leer_cc(cc):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT nombre, apellido, cc FROM usuario WHERE cc = '{0}'".format(cc) 
        cursor.execute(sql)
        datos=cursor.fetchone()
        #cursos = []
        if datos != None:
            curso = {'nombre': datos[0],'apellido': datos[1],'cc': datos[2]}
            #cursos.append(curso)
            return jsonify({'curso':curso,'mensaje':"Usuario Encontrado!."})
        else:
            return jsonify({'curso':curso,'mensaje':"Usuario No Encontrado!."})
    except Exception as e:
     return "error"


@app.route('/cursos/<nombre>')
def leer_name(nombre):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT nombre, apellido, cc FROM usuario WHERE nombre = '{0}'".format(nombre)
        cursor.execute(sql)
        datos=cursor.fetchone()
        
        if datos != None:
            curso = {'nombre': datos[0],'apellido': datos[1],'cc': datos[2]}            
            return jsonify({'curso':curso,'mensaje':"Usuario Encontrado!."})
        else:
            return jsonify({'curso':curso,'mensaje':"Usuario No Encontrado!."})
    except Exception as e:
     return "error"

@app.route('/cursos', methods=['POST'])
def insertar():#funciona
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO usuario (nombre, apellido, cc)
        VALUES ('{0}','{1}','{2}')""".format(request.json['nombre'],request.json['apellido'],request.json['cc'])
        cursor.execute(sql)
        conexion.connection.commit()#confirma la accion de insertar                
        return jsonify({'mensaje':"Registro exitoso."})        
    except Exception as e:
     return "error"

# intentanto crear una tabla
# @app.route('/cursos', methods=['POST'])
# def insertar_tabla():#probando
#     try:
#         cursor = conexion.connection.cursor()
#         sql = """CREATE table materia
#         (nombre_m varchar (50), creditos int)""".format(request.json['nombre_m'],request.json['creditos'])            
#         cursor.execute(sql)
#         conexion.connection.commit()       
#         return jsonify({'mensaje':"Tabla creada."})        
#     except Exception as e:
#      return "error"


def PaginaNoEncontrada(error):
    return "<h1>tuki tuki lu lu...</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, PaginaNoEncontrada)
    app.run()

   #probando git