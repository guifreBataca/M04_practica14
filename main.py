import json

from guifre.Car import Car
from guifre.user import User

cars = [
    Car(4, 758, "opel", "verd"),
    Car(4, 265, "smart", "vermell"),
    Car(4, 265, "citroen", "blau"),
    Car(4, 265, "kia", "groc")
]
cars_list = [c.to_dict() for c in cars]

users = [
    User("masculí", "Guifré", "Salvat", "Pique", "guifre2003", 19),
    User("femení", "Guifresa", "Salvada", "Picada", "guifresa2003", 19),
    User("no binari", "Guifrée", "Salvate", "Piquee", "guifree2003", 19),
    User("massculí", "Gofre", "Salvage", "Picado", "gosapi2003", 19)
]
users_list = [u.to_dict() for u in users]
data = {"cars":cars_list, "users":users_list}

with open("a.json", 'w') as file:
    json.dump(data, file)
