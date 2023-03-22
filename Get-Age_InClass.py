# Morgan Gerdin
# Get age
# due 2/11/2022

def main():
    try:
        Age = int(input("What is your age?"))
        print(f"You are {Age} years old")

    except ValueError:
        print("Error: You must enter a number, not letters")   # specify error


if __name__ == "__main__":  # call main
    main()
