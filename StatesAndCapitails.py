# Morgan Gerdin
# States and Capitails
# Due 2/28/2022


def main():
    stateList = [["iowa", "des moines"], ["kansas","topeka"], [ "minnesota", "st paul"], ["missouri", "jefferson city"],\
                ["nebraska", "lincoln"], ["north dakota", "bismarch"] , ["south dakota", "pierre"], ["wisconsin", "madison"]]

    capital = ""
    try:
        state = input("enter a midwestern state").lower()
        for char in state:
            index = 0
            if char == "iowa":
                index = 0
            elif char == "kansas":
                index = 1
            elif char == "minnesota":
                index = 2
            elif char == "missouri":
                index = 3
            elif char == "nebraska":
                index = 4
            elif char == "north dakota":
                index = 5
            elif char == "south dakota":
                index = 6
            elif char == "wisconsin":
                index = 7
            else:
                break
        #capital = stateList[[index][1]]

        b = [index[1] for index in stateList]
        print(f"The capital for {state} is {b}")

    except ValueError:
        print("an error has occurred: You must enter letters")


if __name__ == "__main__":  # call main
    main()

