import pickle
import dataclasses

@dataclasses
class Student:
    name = ""
    passwors = ""
    login = ""

with open('Solved_tests.txt', 'rb') as f:
    solved = pickle.load(f)

with open('Solved_tests.txt', 'wb') as f:
    pickle.dump(solved, f)
