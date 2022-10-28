"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int=1)-> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    print("Загадано число от 1 до 100")
    min = 0
    max = 100
    while True:
        predict = round((min+max)/2) # предполагаемое число
        count += 1
        if number == predict:
            break # выход из цикла если угадали
        elif number > predict:
            min = predict
            print(f"Угадываемое число больше {predict}")
            print(f'Алгоритм бинарного поиска рекомендует вам число:{round((max + min) / 2)}')
        elif number < predict:
            max = predict
            print(f"Угадываемое число меньше {predict}")
            print(f'Алгоритм бинарного поиска рекомендует вам число:{round((max+min)/2)}')
        elif count >20:
            break
    print(f"Вы угадали число {number} за {count} попыток.")
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
