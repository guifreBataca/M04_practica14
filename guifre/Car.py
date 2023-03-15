
class Car:
    def __init__(self, nRodes, potencia, marca, color):
        self.nRodes = nRodes
        self.potencia = potencia
        self.marca = marca
        self.color = color

    def getNRodes(self):
        return self.nRodes
    def getPotencia(self):
        return self.potencia
    def getMarca(self):
        return self.marca
    def getColor(self):
        return self.color

    def setNRodes(self, nRodes):
        self.nRodes = nRodes

    def setPotencia(self, potencia):
        self.potencia = potencia

    def setMarca(self, marca):
        self.marca = marca

    def setColor(self, color):
        self.color = color

    def info(self):
        print(f"El numero de rodes és: {str(self.nRodes)}")
        print(f"La potència és: {str(self.potencia)}")
        print(f"La marca és: {self.marca}")
        print(f"El color és: {self.color}")

    def to_dict(self):
        return{
            "nRodes": self.nRodes,
            "potencia": self.potencia,
            "marca": self.marca,
            "color": self.color
        }
