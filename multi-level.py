class Animal:
    def __init__(self,  is_bird):
        self.is_bird = is_bird

    def birds_fly(self):
        if self.is_bird:
            return "It is bird"
        else:
            return "It is not bird"

class Birds(Animal):

    def __init__(self,wings,claws,name,color):
        self.wings = wings
        self.claws = claws
        self.name = name
        self.color = color

    def birds_fly(self,is_bird):
        return super(Birds,self).__init__(is_bird)

    def get_bird_name(self):
        return "name of the bird is {} and parrots are {}".format(self.name, self.color)

class Parrot(Birds):

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def birds_fly(self,is_bird):
        return super(Animal,self).__init__(is_bird)


dog = Animal(is_bird=False)
parrot = Birds(2, 2, "parrot", "green")
print(parrot.birds_fly(parrot))
print(parrot.get_bird_name())
print(dog.birds_fly())
