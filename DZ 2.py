class ZOO:
    def __init__(self, name=None, age=None, height=None, weight=None):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f" Name: {self.name} \n Age: {self.age} \n Height:  {self.height} \n Weight: {self.weight}"

    def incrHeight(self):
        self.height = self.height+5

ZOOParrot = ZOO(name = "Parrot", age=3.4, height=30, weight=150)
ZOOCat = ZOO(name = "Cat", age=4.7, height=35, weight=2350)
ZOODog = ZOO(name = "Dog", age=6.3, height=44, weight=3860)
ZOOHamster = ZOO(name = "Hamster", age=0.5, height=11, weight=140)
ZOOFish = ZOO(name= "Fish", age=0.4, height=5, weight=37)
ZOOTurtle = ZOO(name= "Turtle", age=3.5, height=5, weight=470)
ZOOTiger = ZOO(name= "Tiger", age=7.8, height=100, weight=23470)
ZOOGiraffe = ZOO(name= "Giraffe", age=8.4, height=1360, weight=57360)
ZOOFox = ZOO(name= "Fox", age=4.6, height=48, weight=3430)
ZOORabbit = ZOO(name= "Rabbit", age=2.4, height=50, weight=3200)
ZOOZebra = ZOO(name= "Zebra", age=7.3, height=170, weight=14350)
ZOOBear = ZOO(name= "Bear", age=17.1, height=230, weight=83470)
ZOOCamel = ZOO(name= "Camel", age=12.6, height=260, weight=97700)
ZOOElephant = ZOO(name= "Elephant", age=34.9, height=420, weight=1352700)
ZOOGorilla = ZOO(name= "Gorilla", age=23.6, height=230, weight=296000)

print(ZOOParrot)
