# Morgan Gerdin
# Cities in class
# Due 2/18/2022

def main():
    cities = ["Rosevile", "Plymouth", "Maple Grove", "Saint Paul"]      # create list of cities
    location = input("Where would you not like to go?")

    try:
        cities_index = cities.index(location)
        new = input("where would you like to go?")      # get new city
        cities[cities_index] = new
        print("The new list is:")               # print result
        print(cities)

    except ValueError:                                  # capture errors 
        print("That city is not found in the list")


if __name__ == "__main__":  # call main
    main()
