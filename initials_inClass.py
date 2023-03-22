# Morgan Gerdin
# initials in class
# due 2/21/2022 ?


def main():
    name = input("Enter full name:")                    # get full name fom user
    nameList = name.split()                             # put name into list
    for string in nameList:
        print(string[0].upper(), sep="", end="")
        print(".", sep= "", end= "")


if __name__ == "__main__":  # call main
        main()



