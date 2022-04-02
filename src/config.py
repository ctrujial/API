import MySQLdb


class Develomentconfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'tdea'
    MYSQL_PASSWORD = '12345'
    MYSQL_DB = 'api-flask'


config = {
     'development':Develomentconfig
 }