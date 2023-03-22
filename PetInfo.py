# Morgan Gerdin
# In class pet info
from pets import Pet

def main():
    petName = ""
    petType = ""
    petAge = 0

    petName = input("Enter name:")
    petType = input("Enter type:")
    petAge = input("Enter age:")

    mypet = Pet(petName, petType, petAge)

    print("here is your pet:")
    print("_________________________________")
    print(f"Animal name: {mypet.get_Name()}")
    print(f"Animal type: {mypet.get_AnimalType()}")
    print(f"Animal's age: {mypet.get_Age()}")

if __name__ == "__main__":  # call main
    main()