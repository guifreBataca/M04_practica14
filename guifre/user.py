class User():
    def __init__(self, genere, nom, cognom, segonCognom, nomUsuari, edat):
        self.genere = genere
        self.nom = nom
        self.cognom = cognom
        self.segonCognom = segonCognom
        self.nomUsuari = nomUsuari
        self.edat = edat

    def setGenere(self, genereNou):
        self.genere = genereNou

    def setNom(self, nomNou):
        self.nom = nomNou

    def setCognom(self, cognomNou):
        self.cognom = cognomNou

    def setSegonCognom(self, segonCognomNou):
        self.segonCognom = segonCognomNou
    def setNomUsuari(self, nomUsuariNou):
        self.nomUsuari = nomUsuariNou

    def setEdat(self, edatNou):
        self.edat = edatNou

    def getGenere(self):
        return self.genere

    def getNom(self):
        return self.nom

    def getCognom(self):
        return self.cognom

    def getSegonCognom(self):
        return self.segonCognom

    def getNomUsuari(self):
        return self.nomUsuari

    def getEdat(self):
        return self.edat

    def info(self):
        print("El gènere de l'usuari és: " + self.genere)
        print("El nom real de l'usuari és: " + self.nom)
        print("El cognom de l'usuari és: " + self.cognom)
        print("El segon cognom de l'usuari és: " + self.segonCognom)
        print("El nom d'usuari l'usuari és: " + self.nomUsuari)
        print("L'edat de l'usuari és: " + str(self.edat) + "\n")

    def to_dict(self):
        return {
            "gènere": self.genere,
            "nom": self.nom,
            "cognom1": self.cognom,
            "cognom2": self.segonCognom,
            "usuari": self.nomUsuari,
            "edat": self.edat
        }