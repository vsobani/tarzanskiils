class Animal:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"{self.name} eats chicken")

    def sleep(self):
        print(f"{self.name} sleeps all day")

    def attack(self):
        print(f"{self.name} attacks cat")


class Cat(Animal):

    def meow(self):
        print(f"{self.name} is a cat and sounds like meowww ")

    def attack_cat(self):
        print(f"{self.name} attacks rats")


class Dog(Animal):

    def bark(self):
        print(f"the {self.name} barks every day ")


class Fish(Animal):

    def swim(self):
        print(f"{self.name} dives in water")

    def forget(self):
        print(f"{self.name} forgets every now and then")


dog_1 = Dog("aldo", 5, "Male")
cat_1 = Cat("madmax", 2, "Female")
fish_1 = Fish("Nemo", 2, "Female")

Animal.eat(dog_1)
Animal.attack(dog_1)

Cat.meow(cat_1)
Cat.attack_cat(cat_1)

Fish.forget(fish_1)
Fish.swim(fish_1)