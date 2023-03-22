# Morgan Gerdin
# Tuition
# Due 2/28/2022


def main():
    annualTuition = 20000               # make tuition $20,000
    count = 1
    try:
        while count < 6:
            print(f"The tuition is {annualTuition: .2f} for fall of year {count}")          # print results
            annualTuition += annualTuition * .03
            count += 1

    except:
        print("an error has occurred.")



if __name__ == "__main__":  # call main
    main()