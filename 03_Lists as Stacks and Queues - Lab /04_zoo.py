class Zoo:

    __animals = 0

    def __init__(self, name):
         self.name = name
         self.mammals = []
         self.fisher = []
         self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fisher.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1


    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fisher)}\n"
        elif species == 'bird':
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"

        return result

zoo_name = input()
zoo = Zoo(zoo_name)
number = int(input())
x = 0
for x in range(number):
    animal = input().split(' ')
    special = animal[0]
    name = animal[1]
    zoo.add_animal(special, name)

info = input()

print(zoo.get_info(info))
