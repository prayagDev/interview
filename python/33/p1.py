class Animal:

    def eat(self):
        print("Eating...")


class Dog(Animal):

    def bark(self):
        print("Barking...")


class Cat(Animal):

    def meow(self):
        print("Meowing...")


dog = Dog()

dog.eat()     # inherited
dog.bark()

print()

cat = Cat()

cat.eat()     # inherited
cat.meow()

