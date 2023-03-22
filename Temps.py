# MOrgan Gerdin
# temps in class
# due 2/16/2022

def main():
    temp = []
    print("enter low temp")
    for day in range(1, 8):             # make range for 7 days
        low = int(input(f"day {day}:"))
        temp.append(low)                    # add to list

    total = sum(temp)
    average = total/7
    print(f"The average low temp is {average:.2f}")


if __name__ == "__main__":      # call main
    main()

