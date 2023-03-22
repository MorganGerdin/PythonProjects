# Morgan Gerdin
# interstate in class
# due 03/16


def main():
    # create interstate dictionary
    interstate = {"MN": 35, "SF": 80, "SE": 90, "WA": 94, "MI": 95, "TC": 494}
    # filter divisible by two
    eastWest = {k:v for k,v in interstate.items() if v % 2 == 0}
    print(eastWest)
    # filter divisible by five
    importantEastWest = {k:v for k, v in eastWest.items() if v % 5 == 0}
    print(importantEastWest)




if __name__ == "__main__":  # call main
    main()