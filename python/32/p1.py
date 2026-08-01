class CoffeeMachine:

    def __boil_water(self):
        print("Boiling Water")

    def __add_coffee(self):
        print("Adding Coffee")

    def __pour_into_cup(self):
        print("Pouring into Cup")

    def make_coffee(self):
        self.__boil_water()
        self.__add_coffee()
        self.__pour_into_cup()
        print("Coffee Ready ☕")


machine = CoffeeMachine()

machine.make_coffee()

# machine.__boil_water()  