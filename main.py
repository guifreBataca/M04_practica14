# Arxiu main on s'utilizen les classes de aquesta activitat i de la anterior.

import json

from guifre.Car import Car

from guifre.user import User


from Sebastian.Cat import Cat
from Sebastian.School import School

# Es fa una llista amb les instàcies de la classe Car.
cars = [
    Car(4, 758, "opel", "verd"),
    Car(4, 265, "smart", "vermell"),
    Car(4, 265, "citroen", "blau"),
    Car(4, 265, "kia", "groc")
]
# S'emmagatzema la llista de cars en forma de diccionari.
cars_list = [c.to_dict() for c in cars]

# Es fa una llista amb les instàcies de la classe User.
users = [
    User("masculí", "Guifré", "Salvat", "Pique", "guifre2003", 19),
    User("femení", "Guifresa", "Salvada", "Picada", "guifresa2003", 19),
    User("no binari", "Guifrée", "Salvate", "Piquee", "guifree2003", 19),
    User("massculí", "Gofre", "Salvage", "Picado", "gosapi2003", 19)
]
# S'emmagatzema la llista de users en forma de diccionari.
users_list = [u.to_dict() for u in users]
data = {"cars":cars_list, "users":users_list}

cats = [
    Cat("Asiatico","2","naranja","macho"),
    Cat("Siames","1","negro","hembra"),
    Cat("Abisinio","5","plomo","hembra"),
    Cat("birmano","3","blanco","hembra"),
    Cat("Egipcio","4","cafe","macho")
]
cats_list = [ct.to_dict() for ct in cats]

schools = [
    School("7","20","200","220","220","4"),
    School("5","12","75","100","100","4"),
    School("10","25","300","350","350","8"),
    School("6","15","100","150","150","6"),
    School("4","10","50","100","100","4")
]
schols_list = [sh.to_dict() for sh in schools]

data1 = {"cats":cats_list, "schools":schols_list}

with open ("json_API/b.json", 'w') as file:
    json.dump(data1, file)

# S'agrupen els dos diccionaris
data = {"cars":cars_list, "users": users_list}

# Es transformen en foormat json i s'escriu a l'arxiu.
with open("a.json", 'w') as file:
    json.dump(data, file)
