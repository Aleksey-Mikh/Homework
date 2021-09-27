class BeAbleToFly:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} can fly, but it won't fly too close to the sun"

    def fly(self):
        return f"{self.name} can fly"


class BeAbleToWalk:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} can walk, but born to walk will never fly"

    def walk(self):
        return f"{self.name} can walk"


class BeAbleToSwim:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} it can swim, but can it dive?"

    def swim(self):
        return f"{self.name} bird can swim"


class BeAbleToEat:

    def __init__(self, ration):
        self.ration = ration

    def __str__(self):
        return f"{self.ration} is delicious"

    def eat(self):
        return f"It eats mostly {self.ration}"


class Bird(BeAbleToWalk, BeAbleToFly):

    def __str__(self):
        return f"{self.name} can walk and eat"


class FlyingBird(Bird, BeAbleToEat):

    def __init__(self, name, ration="insects"):
        self.ration = ration
        super().__init__(name)

    def __str__(self):
        return f"{self.name} can walk and fly"


class NonFlyingBird(BeAbleToWalk, BeAbleToSwim, BeAbleToEat):

    def __init__(self, name, ration="fish"):
        self.ration = ration
        super().__init__(name)

    def __str__(self):
        return f"{self.name} can walk and swim"


class SuperBird(FlyingBird, BeAbleToSwim):

    def __init__(self, name, ration="people"):
        self.ration = ration
        super().__init__(name, ration)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly like a dragon"


c = FlyingBird("Canary", "charry")
print(c.eat())
print(c.walk())
print(c.fly())

p = NonFlyingBird("Penguin", "asd")
print(p.swim())
# print(p.fly())
print(p.eat())


s = SuperBird("Gull", "people")
print(str(s))
print(s.eat())
print(s.walk())
print(s.swim())
print(s.fly())
print(SuperBird.__mro__)
