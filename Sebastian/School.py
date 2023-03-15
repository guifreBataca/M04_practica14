class School:
    def __init__(self, aulas, maestros, alumnos, mesas, sillas, baños):
        self.aulas = aulas
        self.maestros = maestros
        self.alumnos = alumnos
        self.mesas = mesas
        self.sillas = sillas
        self.baños = baños
    def getAulas(self):
        return self.aulas
    def setAulas(self, aulas):
        self.aulas = aulas
    def getMaestros(self):
        return self.maestros
    def setMaestros(self, maestros):
        self.maestros = maestros
    def getAlumnos(self):
        return self.alumnos
    def setAlumnos(self, alumnos):
        self.alumnos = alumnos
    def getMesas(self):
        return self.mesas
    def setMesas(self, mesas):
        self.mesas = mesas
    def getSillas(self):
        return self.sillas
    def setSillas(self, sillas):
        self.sillas = sillas
    def getBaños(self):
        return self.baños
    def setBaños(self, baños):
        self.baños = baños
    def info(self):
        print("Tienen: " + self.aulas)
        print("Tienen: " + self.maestros)
        print("Tienen: " + self.alumnos)
        print("Tienen: " + self.mesas)
        print("Tienen: " + self.sillas)
        print("Tienen: " + self.baños + "\n")
    def to_dict(self):
        return {
            "aulas":self.aulas,
            "maestros":self.maestros,
            "alumnos":self.alumnos,
            "mesas":self.mesas,
            "sillas":self.sillas,
            "baños":self.baños
        }