"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

res_list = []
while True:
    user_input = input("Введите целое число для формирования рейтинга: ").split(" ")

    '''Проверка на int'''
    for i in user_input:
        try:
            res_list.append(int(i))
        except ValueError:
            raise ValueError("Введённое значение не является int")
    '''Проверка на int'''

    res_list.sort(reverse=True)
    print(f"Пользователь ввел число {user_input}. Результат: {res_list}.")

'''
el1 = 0
while len(res_list) > el1+1:
    res_list[el1], res_list[el1+1] = res_list[el1+1], res_list[el1]
    el1 += 2
print(res_list)
'''