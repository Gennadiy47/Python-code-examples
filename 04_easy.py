# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

l = [1, 2, 4, 0]
new_l = [x ** 2 for x in l]

print(new_l)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

l1 = ['яблоко', 'апельсин', 'банан', 'кокос']
l2 = ['апельсин', 'мандарин', 'кокос', 'клементин']

total = [x for x in l1 if x in l2 ]
print(total)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

l = [random.randint(-5, 20) for _ in range(10)]
print(l)
result = [x for x in l if x % 3 == 0 and x >= 0 and x % 4 != 0]
print(result)