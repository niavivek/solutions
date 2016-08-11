# Task: modify script from problem D06ex03.py to write results to a
# file


def count_names_write():
    names_with_e_count = 0
    names_with_e_list = list()
    with open("roster.txt", "r") as roster:
        name_lines = roster.readlines()
    for name in name_lines:
        first_name = name.split()[0]
        if "e" in first_name:
            names_with_e_list.append(first_name)
            names_with_e_count += 1
    with open("names_with_e.txt", "w") as names_with_e:
        names_with_e.write("{} names contain the letter 'e'".format(
                            names_with_e_count))
        for name in names_with_e_list:
            names_with_e.write("\n"+name)


def main():
    count_names()

if __name__ == "__main__":
    main()
