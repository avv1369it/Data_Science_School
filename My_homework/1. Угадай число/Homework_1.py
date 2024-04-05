"""
Project_0 - "Игра угадай число"
Компьютер задает случайное число и самостоятельно его находит.
Максимальное количество шагов должно быть не больше 20.
 
"""

import numpy as np

def random_predict(number:int=1) -> int:    
    """
    Определяем число.
    Args:
        number(int, optional): начальное число которое сравнивается с загадоным, изначально определено 1.
    Returns:
        counts: количество шагов
    """
    count = 0
    min_number = 1
    max_number = 100
    predict_number = np.random.randint(1, 101) # функция возвращает случайное целое число из диапазона 1 - 100 (включительно)
    
    while True:
        count += 1 
        if number == predict_number:
            break # выход из цикла, если число угадано
        
        elif predict_number > number:
            max_number = predict_number
            predict_number = int((min_number + max_number)/2)
            
        elif predict_number < number:
            min_number = predict_number
            predict_number = int((min_number + max_number)/2)
        
        if count > 50: # ввод ограничения для выхода из цикла while
            break
            
    return(count)

def score_game(random_predict) -> int:
    """
    За какое количество попыток алгоритм определяет число при количестве повторений - 1000.
    
    Args:
        random_predict ([type]): функция определения числа
    Returns:
        count: среднее количество шагов
    """
    
    count_ls = [] # формируем список для сохранения количества попыток
    np.random.seed(13) # задаем начальное состояние генератора
    random_array = np.random.randint(1, 100, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f"Текущий алгоритм определяет число в среднем за: {score} шагов.")
    
    return(score)

score_game(random_predict)
