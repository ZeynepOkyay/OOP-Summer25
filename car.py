class Car:
    def __init__(self):
        self.brand = "Toyota"
        self.__engine = "Hybrid"

    def show_engine(self):
        print("Engine:", self.__engine)

    def __start_the_engine(self):
        print("Engine started")

    def start_the_car(self):
        self.__start_the_engine()

my_car = Car()
print("Brand:", my_car.brand)

my_car.show_engine()
my_car.start_the_car()