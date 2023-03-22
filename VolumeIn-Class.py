# Morgan Gerdin
# Volume in-class
# due: 2/4/2022

def main():
    Length = int(input("what is the length?"))
    Width = int(input("what is the Width?"))
    Height = int(input("what is the Height?"))
    Answer = Volume(Length, Width, Height)
    print(Answer)


def Volume(Length, Width, Height):
    Answer = Length * Width * Height
    return Answer


main()