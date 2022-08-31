import mysql.connector
import datetime

class Dal():
    def __init__(self) -> None:
        self.db_user = 'root'
        self.db_password = 'Ximenes34!'
        self.db_host = '127.0.0.1'
        self.db_database = 'charada'



    def open(self):
        try:
            self.connection = mysql.connector.connect(user= self.db_user, password = self.db_password, host = self.db_host, database = self.db_database)
            self.cursor = self.connection.cursor(dictionary=True)
        except:
            print("Could not open connection. Check DAL")
            pass

    def close(self):
        try:
            self.connection.close()
        except:
            print("Connection alredy closed.")



