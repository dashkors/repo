

class Animals:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        if self.type == "beast":
            self.cell = "_aviary for beasts_"
        elif self.type == "fish":
            self.cell = "_aquarium_"
        elif self.type <> "bird":
            self.cell = "_cell_"
        else:
            self.cell = "_cage for birds_"

    def printinfo(self):
        print("Питомец:" , self.name , "-" , self.type, "Живет в ", self.cell)


class Iterator:
    def iterateAni(self):
        listname = ["Аист", "Белый слон", "Шимпанзе", "Лев", "Золотая рыбка"]
        listtype = ["bird" , "beast" , "beast", "beast", "fish"]
        for i in range(0, 4):
            ani = Animals(listname[i] , listtype[i])
            ani.printinfo()


def main():
    print ('гууд')
    iterator = Iterator()
    iterator.iterateAni()


print("Животные в зоопарке:")
if __name__ == "__main__":
    main()
