from time import sleep
from threading import Thread


def car(velocity, pilot):
    trage = 0
    while trage <= 100:
        print(f"Car [{pilot}] {trage}")
        trage += velocity
        sleep(.5)


t_car_1 = Thread(target=car, args=[1, "Foo"])
t_car_2 = Thread(target=car, args=[2, "Bar"])

t_car_1.start()
t_car_2.start()