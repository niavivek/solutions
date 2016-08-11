# Task: create a script that performs these tasks:
# - change to directory with your assignments/labs, print the path
# - print names of your python files


import os


def list_files():
    os.chdir("/Users/dsg/_pbc-2016/D05")
    print("Path: " + os.getcwd())
    print("Python files are:")
    for file_name in os.listdir():
        if file_name.endswith(".py"):
            print("\t"+file_name)


def main():
    list_files()

if __name__ == "__main__":
    main()
