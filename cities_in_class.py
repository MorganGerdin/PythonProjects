# Morgan Gerdin
# cities in class
# due 03/16


def main():
    cities = {"Nairobi": 1, "Johannesburg": 26, "Cairo": 30, "Abidjan": 5, "Khartoum": 15, "Zanzibar": 6}

    # first attempt

    # tropic = {k:v for k,v in cities.items() if v < 24}
    # for key,value in tropic.items():
    #     print(key,value)

    # create empty dictionary
    tropics = {}
    for k, v in cities.items():
        if v < 23:
            tropics[k] = v

    # print results
    print(tropics)


if __name__ == "__main__":  # call main
    main()