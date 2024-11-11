import threading
import random
import time

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        self.lock.acquire()
        for i in range (100):
            rand_dopsum = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += rand_dopsum
            print(f'Пополнение: {rand_dopsum}. Баланс: {self.balance}')
        time.sleep(0.001)


    def take(self):
        for i in range (100):
            rand_dopsum = random.randint(50, 500)
            print(f'Запрос на {rand_dopsum}')
            if rand_dopsum <= self.balance:
                self.balance -= rand_dopsum
                print(f'Снятие: {rand_dopsum}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')