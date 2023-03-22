# Morgan Gerdin
# Credit card account verification
# due 2/28/2022


def main():
    cardNumber = input("Enter a credit card number:")
    infile = open("credit_card.txt", "r")
    readfile = infile.read()
    count = 0
    numCount = 1
    for char in cardNumber:
        numCount += 1

    if 9 > numCount > 7:
        for char in readfile:
            for char in cardNumber:
                if char in cardNumber:
                    count += 0
                else:
                    count += 1
        if count == 0:
            print("the credit card is valid")
        else:
            print("the card in not valid")

    else:
        print("the card must have 7 numbers")


if __name__ == "__main__":  # call main
    main()