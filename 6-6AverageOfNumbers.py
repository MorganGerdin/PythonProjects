# morgan Gerdin
# in class read file
# due 2/9/2022

def main():
    count = 0           # track total count of numbers
    number = 0          # track number of numbers in file
    infile = open("numbers.txt", "r")
    for line in infile:
        count += int(line)
        number += 1
    Average = count / number        # find average
    print(F"{Average: .2f}")


if __name__ == "__main__":          # call main
    main()