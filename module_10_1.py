import time
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range (1, word_count + 1):
            f.write(f'Какое-то слово №{i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f"Работа потоков {time_res}")

time_start = datetime.now()

threads = [
    Thread(target=write_words, args=(10, 'example5.txt')),
    Thread(target=write_words, args=(30, 'example6.txt')),
    Thread(target=write_words, args=(200, 'example7.txt')),
    Thread(target=write_words, args=(100, 'example8.txt'))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

time_end = datetime.now()
time_res = time_end - time_start
print(f"Работа потоков {time_res}")