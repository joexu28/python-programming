class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


#point1 = Point()
#point1.x = 10
#point1.y = 20
#print(point1.x)
#point1.draw()

point2 = Point(10, 20)
print(point2.x)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi I am {self.name}")


person = Person("john Smith")
person.talk()

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def cute(self):
        print("cute")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.cute()
