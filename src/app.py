from asyncio import Task, tasks
from sqlite3 import Cursor
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

# @app.route('/task',methods = ['POST'])/// no reconoce methods**
# def crear_tablas():
#     titulo = request.json['titulo']
#     descrpcion = request.json['descripcion']

#     new_Task = Task(titulo, descrpcion)
#     conexion.session.add(new_Task)
#     conexion.session.commit()
    

def PaginaNoEncontrada(error):
    return "<h1>tuki tuki lu lu...</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, PaginaNoEncontrada)
    app.run()

   #probando git