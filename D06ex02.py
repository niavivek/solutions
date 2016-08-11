# Task: write ten random numbers to a file

import random


def write_random_numbers():
    with open("random_numbers.txt", "w") as fout:
        for each in range(10):
            fout.write(str(random.randint(1, 1000))+"\n")


def main():
    write_random_numbers()

if __name__ == "__main__":
    main()
