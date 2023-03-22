#Morgan Gerdin
# product in-class
# due: 2/4/2022
def main():
    int1 = int(input("what is the first integer?"))     # get integers
    int2 = int(input("what is the second integer?"))
    calc(int1, int2)


def calc(int1, int2):    # calculate answer
    Answer = int2 * int1
    print(Answer)


main()  # call main function