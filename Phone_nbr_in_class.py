# Morgan Gerdin
# phone number in class
# due 2/23/2022


def main():
    number = input("enter a phone number").upper()          # convert all letters to upper
    newNumber = ""
    nums = ['2', '3', '4', '5', '6', '7', '8', '9']
    for char in number:                                     # loop through number
        index = None
        if char.isalpha():
            if char == "A" or char == "B" or char == "C":
                index = 0
            elif char == "D" or char == "E" or char == "F":
                index = 1
            elif char == "G" or char == "H" or char == "I":
                index = 2
            elif char == "J" or char == "K" or char == "L":
                index = 3
            elif char == "M" or char == "N" or char == "O":
                index = 4
            elif char == "P" or char == "Q" or char == "R" or char == "S":
                index = 5
            elif char == "V" or char == "T" or char == "U":
                index = 6
            elif char == "W" or char == "X" or char == "Y" or char == "Z":
                index = 7

            newNumber += nums[index]
        else:
            newNumber += char
    print(newNumber)


if __name__ == "__main__":  # call main
    main()
