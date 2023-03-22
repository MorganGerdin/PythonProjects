# Morgan Gerdin
# employee_count in-class
# due: 2/4/2022

count = 0  #initialize count
def main():
    FirstName = input("What is the first name?")    # get names
    LastName = input("What is the last name?")
    employee(FirstName, LastName)


def employee(name1, name2):
    global count
    count += 1     # give each employee a unique ID

    print("Employee: ", name1 + " ", name2)
    print("EmployeeID: ", str(count))


if __name__ == "__main__":
    main()
