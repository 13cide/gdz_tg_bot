import pickle
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    login: str
    password: str

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password


aleksey = Student("Aleksey", "1711ymk492", "AByRH9")
meliha = Student("Meliha", "", "")
georgiy = Student("Georgiy", "", "")
artemiy = Student("Artemiy", "", "")

students = [aleksey, meliha, georgiy, artemiy]

solved = []

# with open('Solved_tests.txt', 'wb') as f:
#     pickle.dump(solved, f)


tg_token = "5604783662:AAFVXbNTPmjBwCqgUxx7qMb1fP29LzWsOxs"

chat_id = -893219349