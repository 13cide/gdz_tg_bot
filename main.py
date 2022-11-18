import config
import pickle


def solve():
    with open('Solved_tests.txt', 'wb') as f:
        pickle.dump(config.solved, f)


def main():
    # some_parsing   TODO
    solve()


if __name__ == '__main__':
    main()
