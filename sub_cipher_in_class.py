# Morgan Gerdin
# sub cipher
# due 2/23/2022


def main():
    message = input("enter a message")          # get message
    encipher = decipher = ""
    for char in message:                        # encode message
        encipher += chr(ord(char) + 5)
    print(encipher)
    Question = input("Would you like to decipher? (y/n)")       #  ask user if they want to decipher
    if Question == "y":
        for char in encipher:                   # decode message
            decipher += chr(ord(char) -5)
        print(decipher)



if __name__ == "__main__":  # call main
    main()
