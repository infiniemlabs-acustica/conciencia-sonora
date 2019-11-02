'''
aca van todo lo que son operaciones.
para consultar la base
'''
import mysql.connector

class DB:
    
    def __init__(self):
        try:
            self.connect = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "cslogin")
            self.cursor = self.connect.cursor()
        
        except Exception as e:
            raise e
    
    def insert(self,query,values):
        try:
            self.cursor.execute(query,values)
            self.connect.commit()

            #lastrowid hace referencia al id que se inserto  PK, A_I
            return self.cursor.lastrowid
            
        except Exception as e:
            raise e

    def getWhere(self,query,values):
        try:
            # 1. execute (consulta a ejecutar)
            # 2. retorna el result SQL
            self.cursor.execute(query,values)
            
            return self.cursor.fetchone()
            
        except Exception as e:
            raise e

if __name__ == "__main__":
    # Instanciar pruebas

    db = DB()