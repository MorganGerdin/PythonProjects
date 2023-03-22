# morgan Gerdin
# in class read file
# due 2/9/2022

def main():             #define main
    infile = open("titles.txt", "r")
    file_contents = infile.read()
    infile.close()
    print(f'{file_contents}')


if __name__ == "__main__":    # call main
    main()
