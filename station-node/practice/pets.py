
if __name__ == '__main__':
    Main()

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) #you can run superclass methods like this

def Main():
    thePet = Pet("Pet", 1)
    jess = Cat("jess", 3)

    print("Is jess a Cat? "+ str(isinstance(jess, Cat)))
    print("Is jess a Pet? " + str(isinstance(jess, Pet)))
    print("Is thePet a Cat? " + str(isinstance(thePet, Cat)))
    print("Is thePet a Pet? " + str(isinstance(thePet, Pet))
