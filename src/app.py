from sqlite3 import Cursor
from flask import Flask
from flask_mysqldb import MySQL
from config import config

app=Flask(__name__)

conexion=MySQL(app)

@app.route('/cursos')
def listar_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, codigo FROM curso"
        cursor.execute(sql)
        datos=cursor.fetchall()
        print(datos)
        return "ok"
    except Exception as ex:
     return "error"

def PaginaNoEncontrada(error):
    return "<h1>tuki tuki lu lu...</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, PaginaNoEncontrada)
    app.run(debug=True)

    #    paso a paso para crear el entorno virtual

# 1. python -m venv nombre que queramos (en mi caso api-flak_mysql)
# 2.aca activamos el entorno virtual: .\api-flak_mysql\Scripts\activate
# 3.instalamos flask: pip install flask flask_mysqldb
# 4.python .\src\app.py
# .\entornoVirtual\Scripts\activate