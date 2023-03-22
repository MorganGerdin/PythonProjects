# morgan Gerdin
# in class read file
# due 2/9/2022

def main():
    #get movies
    Movie1 = input("enter a movie")
    Movie2 = input("enter a movie")
    Movie3 = input("enter a movie")
    Movie4 = input("enter a movie")
    # add movies to file
    outfile = open('movies.txt', 'a')
    outfile.write(f"{Movie1} \n")
    outfile.write(f"{Movie2} \n")
    outfile.write(f"{Movie3} \n")
    outfile.write(f"{Movie4} \n")
    outfile.close()
    #read file
    infile = open("movies.txt", "r")
    for line in infile:
        line = infile.readline()
    #file_contents = infile.read()
    # print(file_contents)
        print(line)

    infile.close()

 # call main
if __name__ == "__main__":
    main()
