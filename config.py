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

with open('Solved_tests.txt', 'rb') as f:
    solved = pickle.load(f)

