# Task: write a function that reads from roster.txt prints the
# following information to the command line:
#  a. how many names contain the letter ‘e’
#  b. then lists the names which contain the letter ‘e’


def count_names():
    names_with_e_count = 0
    names_with_e_list = list()
    with open("roster.txt", "r") as roster:
        name_lines = roster.readlines()
    for name in name_lines:
        first_name = name.split()[0]
        if "e" in first_name:
            names_with_e_list.append(first_name)
            names_with_e_count += 1
    print("{} names contain the letter 'e'".format(names_with_e_count))
    for name in names_with_e_list:
        print(name)


def main():
    count_names()

if __name__ == "__main__":
    main()
