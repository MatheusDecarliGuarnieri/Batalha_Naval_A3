import mysql.connector

database_connection = mysql.connector.connect(
   host="localhost",
   port="3306",
   user="root",
   password="",
   database="sistema"
)

class JogadorDB():
    _lista = []

    def jogadores_banco(self):
        cursor = database_connection.cursor()
        consulta_banco = "SELECT username FROM auth_user"

        cursor.execute(consulta_banco)
        resultados = cursor.fetchall()
        for resultados in resultados:
            self._lista.append(resultados)

    def __init__(self):
        self.jogadores_banco()


    def lista_todos_os_jogadores(self):
        return self._lista
        