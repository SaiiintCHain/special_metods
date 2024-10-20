class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floor):
        if new_floor > self.floors or new_floor < 1:
            print ("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __str__(self):
        return(f"Название: {self.name},кол-во этажей {self.floors}")

    def __len__(self):
        return self.floors



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))