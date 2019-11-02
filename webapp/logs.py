'''
para ver todo lo que pasa en la web app
erores en tiempo de ejecucion
'''

from datetime import datetime

class Logs:
    
    def __init__(self):
        try:
            self.ruta = "logs.txt"
            # read, write, append
            # open
            self.modoA = "a+" # append
            self.modoR = "r+"

        except Exception as e:
            raise e
        
    def appendFile(self, oracion):
        try:
            self.file = open(self.ruta, self.modoA)
            self.file.write(oracion + " " + str(datetime.now())+"\n")
            
        except Exception as e:
            raise e
            
    def readFile(self):
        try:
            self.file = open(self.ruta, self.modoR)
            for a in self.file:
                print(a)
            
        except Exception as e:
            raise e
               
if __name__ == "__main__":
# Instanciar pruebas

    log = Logs()
    #log.appendFile('hola')
    log.readFile()