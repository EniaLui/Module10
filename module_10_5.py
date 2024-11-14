import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line.strip())
            line = file.readline()

if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    # 2. Вызовите функцию read_info для каждого файла по очереди (линейно)
    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    linear_duration = datetime.now() - start_time
    print(f"{linear_duration} (линейный)")

    # 3. Вызовите функцию read_info для каждого файла, используя многопроцессный подход:
    start_time = datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)

    multiprocess_duration = datetime.now() - start_time
    print(f"{multiprocess_duration} (многопроцессный)")