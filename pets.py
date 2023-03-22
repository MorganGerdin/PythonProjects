class Pet:
    def __init__(self, name, animalType, age):
        self.__name = name
        self.__animalType = animalType
        self.__age = age

    def set_Name(self, name):
        self.__name = name

    def set_AnimalType(self, animalType):
        self.__animalType = animalType

    def set_Age(self, age):
        self.__age = age

    def get_Name(self):
        return self.__name

    def get_AnimalType(self):
        return self.__animalType

    def get_Age(self):
        return self.__age
