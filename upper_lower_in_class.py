# Morgan Gerdin
# upper lower in class
# due 2/21/2022


def main():
    sentence = input("Enter a name")                # get name
    result = " "
    result = result + sentence[0]
    for i in range(1, len(sentence)):
        char = sentence[i]
        if char.isupper():
            char = char.lower()                     # convert upper to lower
            result = result + " "                      # add a space 

        result = result + char

    print(result)



if __name__ == "__main__":  # call main
    main()