import MySQLdb


class Develomentconfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'database'


config = {
     'development':Develomentconfig
 }