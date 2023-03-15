class Cat:
    def __init__(self, raza, edad, color, genero):
        self.raza = raza
        self.edad = edad
        self.color = color
        self.genero = genero
    def getRaza(self):
        return self.raza
    def setRaza(self, raza):
        self.raza = raza
    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad
    def getTamaño(self):
        return self.color
    def setTamaño(self, color):
        self.color = color
    def getGenero(self):
        return self.genero
    def setGenero(self, genero):
        self.genero = genero
    def nom_info(self):
        print("La raza es: " + self.raza)
        print("La edad es: " + self.edad)
        print("El color es: " + self.color)
        print("El genero es: " + self.genero)
    def to_dict(self):
        return {
            "raza":self.raza,
            "edad":self.edad,
            "tamaño":self.color,
            "genero":self.genero
        }
    """"
    cats = [
        Cat("Asiático","2","naranja","macho"),
        Cat("Siames","1","negro","hembra"),
        Cat("Abisinio","5","plomo","hembra"),
        Cat("birmano","3","blanco","hembra"),
        Cat("Egipcio","4","cafe","macho")
    ]
    """
