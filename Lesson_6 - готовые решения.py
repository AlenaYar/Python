# 1) ====================================================================================================

import time


class Trafficlight:
    __color = None

    def start(self):
        while True:
            print(f"\r{'RED'}", end="")
            time.sleep(7)
            print(f"\r{'YELLOW'}", end="")
            time.sleep(2)
            print(f"\r{'GREEN'}", end="")
            time.sleep(7)
            print(f"\r{'YELLOW'}", end="")
            time.sleep(2)


t = Trafficlight()
t.start()


# 2) ====================================================================================================

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def my_r(self):
        return f"{self._width}м * {self._length}м * 25кг * 5см = {int((self._width * self._length * 25 * 5) / 1000)}т"


road_1 = Road(5000, 20)
print(road_1.my_r())

# 3) ====================================================================================================

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"


worker_1 = Position("Иван", "Рыбкин", "Программист", 90000, 50000)
print(worker_1.get_full_name())
print(worker_1.position)
print(worker_1.get_total_income())

# 4) ====================================================================================================

# 5) ====================================================================================================

class Stationery:
    def __init__(self, title=""):
        self.title = title

    def draw(self):
        print(f"Start drawing {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen")


class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil")


class Handle(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} handle")


a = Stationery()
a.draw()
pen = Pen("blue")
pen.draw()
pencil = Pencil("green")
pencil.draw()
handle = Handle("red")
handle.draw()
