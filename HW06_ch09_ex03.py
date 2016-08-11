# write a function that reads from roster.txt prints the following information to the command line:
# a. how many first names contain the letter ‘e’
# b. then lists the first_names which contain the letter ‘e’


def find_the_e():
    count = 0
    list_of_names = []
    file = open("roster.txt", "r")
    new_list = file.readlines()
    for line in new_list:
        line = line.split()
        if len(line) > 2:
            line = line[:-1]
            print(type(line))
            for element in line:
                if "e" in element or "E" in element:
                    count += 1
                    list_of_names.append(element)
        else:
            if "e" in line[0] or "E" in line[0]:
                count += 1
                list_of_names.append(line[0])
    print(count)
    print(list_of_names)
    file.close()


def main():
    find_the_e()

if __name__ == '__main__':
    main()