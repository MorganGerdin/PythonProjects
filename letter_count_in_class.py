# Morgan Gerdin
# letter count in class
# due 2/21/2022


def main():
    count = 0
    name = input("Enter a name")                # get name

    for char in name:                               # loop through name
        if char == "m" or char == "M":
            count += 1
        

    print(f"The letter m appears {count} times")

if __name__ == "__main__":  # call main
    main()