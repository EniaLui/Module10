import time
from threading import Thread

class Knight(Thread):
    enemy = 100

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print (f'{self.name}, на нас напали!')
        day_fight = 0
        while self.enemy > 0:
            day_fight += 1
            self.enemy -= self.power
            if self.enemy < 0:
                self.enemy = 0
            else:
                print (f'{self.name} сражается {day_fight} дней (дня)..., осталось {self.enemy} воинов.')
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {day_fight} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")