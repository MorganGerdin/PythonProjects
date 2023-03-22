# Morgan Gerdin
# Friends
# due 2/16/2022

def main():
    friends = ["Bob", "Ana", "Morgan", "Carly", "Peter"]
    index = 0
    while index < len(friends):         # print original names
        print(friends[index])
        index += 1

    print()
    friends[3] = "Mike"         # change
    friends[4] = "Sally"

    index = 0
    while index < len(friends):             # print new names
        print(friends[index])
        index += 1


if __name__ == "__main__":  # call main
    main()