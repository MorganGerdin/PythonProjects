# Morgan Gerdin
# courses in class
# due 2/16/2022

def main():
    course = ["COS2005", "COS2001", "COS2003", "COS2004","COS2002", "MIS3001", "MIS3002", "MIS3003", "MIS3004", "MIS3005"]
    id = input("enter a course ID:")            # get id from user
    if id in course:        #check if id is in list
        print("The course is in the list")
    else:
        print("The course is not in the list")


if __name__ == "__main__":  # call main
    main()