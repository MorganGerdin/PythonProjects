# Morgan Gerdin
# Sales in class
# due 2/18/2022


def main():
    week = 1            # declare vairables
    total = 0
    sales = [[123, 35, 674, 567, 89],
             [45, 352, 244, 345, 56],
             [53, 34, 674, 345, 133],
             [243, 353, 34, 57, 35]]

    for row in sales:
        for item in row:            # add all items for each week
            total += item

        sum = str(total)
        print(f"Week {week} total: {sum}")
        week += 1
        total = 0


if __name__ == "__main__":  # call main
    main()

