class Persona():

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self,edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def caminar(self):
        return "estoy caminando"    

class Informatico(Persona):
    def __init__(self): 
        self.lenguages = "HTML,Java,PHP,CSS"
        self.experienca = 5
        
    def getLenguages(self):
        return self.lenguages

    def apender(self,lenguages):
        self.lenguages = self.lenguages + ", " + lenguages 
        return self.lenguages
    
    def programar(self):
        return "estoy programando"

    def reparar(self):
        return "estoy arreglando"

class Tenico(Informatico):

    def __init__(self):
        super().__init__()
        self.audita = "experto"
        self.esperiencia = 5

    def queHace(self):
        return "estoy auditando"