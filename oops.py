class Company:

    def __init__(self):
        self.name = "My company"
        self.ceo = "Vishal"
        self.profit = 12.5
        self.established = 1995

    country="India"

    def show_details(self):
        print("The name of the company is", self.name)
        print("The ceo of the company is", self.ceo)

    @classmethod
    def change_location(cls, country):
        cls.country = country

    def show_revenue(self):
        print("The profit is ", self.profit)
        print("The company was established in", self.established)


apple = Company()


microsoft = Company()


print(apple.show_details())
print(apple.show_revenue())


# print(apple.change_location(apple.country))
print("The company is in",apple.country)


print(microsoft.change_location("Usa"))
print(f"The  company is situated in {microsoft.country}")


class laptop:

    def __init__(self,brand,size,price,ceo=None):
        self.brand=brand
        self.size=size
        self.price=price
        self.ceo=ceo


dell=laptop("Dell Inc",12,100000)


print("The brand of the lap[top is ",dell.brand)
print(f"The laptop comes in {dell.size} inches")
print(f"the price of the laptop is {dell.price}")
print(f"the ceo of the company is {dell.ceo}")

hp=laptop("HP",1,12000)

print(hp.brand)
print(hp.size)
print(hp.price)

