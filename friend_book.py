# Morgan Gerdin
# friend book 2 in class
# due 03/16/2022


def main():
    # create the dictionary
    friend_book = {"Bob": "Plymouth", "Morgan": "Plymouth", "Pizza Hut": "Saint Paul", "Sara": "Maple Grove",
                   "Ana B": "Savage", "Chic-Fil-A": "Maple Grove", "Peter": "Plymouth"}

    for key, value in friend_book.items():
        print(key, value)

    print()
    # add two entries
    friend_book["Kile"] = "Blaine"
    friend_book["horse"] = "Barn"
    # display results
    for key,value in friend_book.items():
        print(key, value)

    print()
    # Delete two entries
    del friend_book["Pizza Hut"]
    del friend_book["Bob"]
    # display results
    for key,value in friend_book.items():
        print(key, value)


if __name__ == "__main__":  # call main
    main()
