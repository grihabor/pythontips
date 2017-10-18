from itertools import product
from pprint import pprint
from decimal import Decimal
from collections import Counter


# У игрального кубика 6 граней
options = range(1, 7)

# Сгенерируем все тройки граней, которые выпадут
# если бросить кубик 3 раза
outcomes = product(options,  repeat=3)
# Заметим, что product возвращает генератор, поэтому
# нам не нужно хранить все тройки в памяти

# Посчитаем сумму каждой тройки
sum_outcomes = (sum(outcome) for outcome in outcomes)
# Нам не нужен весь список, поэтому достаточно
# использовать generator expression

# Посчитаем, сколько раз встречается каждая тройка
c = Counter(sum_outcomes)

# Посчитаем количество всех троек как сумму появлений
# каждой тройки
outcome_count = sum(c.values())

# Посчитаем распределение нашей дискретной случайной
# величины, т.е. вероятность выпадания каждой тройки
distribution = {
    key: value / outcome_count 
    for key, value in c.items()
}
# По сути, посчитаем долю появлений каждой тройки
# от общего числа появлений

pprint(distribution)

