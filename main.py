import json

from guifre.Car import Car
from Sebastian.Cat import Cat
from Sebastian.School import School
cars = [
    Car(4, 758, "opel", "verd"),
    Car(4, 265, "smart", "vermell")
]
cars_list = [c.to_dict() for c in cars]

# AQUI VAN GATOS

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


data = {"cars":cars_list} #Añadir aqui

with open("a.json", 'w') as file:
    json.dump(data, file)
