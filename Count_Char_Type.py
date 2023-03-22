# Morgan Gerdin
# Count char type
# Due 2/23/2022


def main():
    upper = lower = space = digits = 0              # set counts to 0
    readFile = ""
    infile = open("text.txt", "r")
    readFile = infile.read()
    for char in readFile:

        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1
        if char.isdigit():
            digits += 1
        if char.isspace():
            space += 1

    infile.close()                  # close file

    print("Uppercase", upper)               # print results
    print("lowercase", lower)
    print("Digits", digits)
    print("Spaces", space)


if __name__ == "__main__":  # call main
    main()