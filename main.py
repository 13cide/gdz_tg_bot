import config
import pickle

from parsing import start_parsing
from config import aleksey

def solve():
    with open('Solved_tests.txt', 'wb') as f:
        pickle.dump(config.solved, f)


def main():
    #with open('Solved_tests.txt', 'rb') as f:
     #   solved = pickle.load(f)

    login = aleksey.login
    password = aleksey.password

    parsing = start_parsing.Parsing()
    parsing.start_parsing(login, password)
    solve()


if __name__ == '__main__':
    main()
