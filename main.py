import json

from guifre.Car import Car

cars = [
    Car(4, 758, "opel", "verd"),
    Car(4, 265, "smart", "vermell")
]
cars_list = [c.to_dict() for c in cars]

# AQUI VAN GATOS

data = {"cars":cars_list} #Añadir aqui

with open("a.json", 'w') as file:
    json.dump(data, file)
