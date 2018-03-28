# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def personal(name, age, city):
    print('{}, {} год(а), проживает в городе {}'.format(name, age, city))


personal('Василий', '21', 'Москва')


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def maximum(x, y, z):
    numbers = [x, y, z]
    return max(numbers)


print(maximum(200, 200, 20))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def infinity(*args):
    return max(args, key=len)

print(infinity('qweqweqwe', 'asdfadfasf', 'dgfhdfgh', 'fdgh', 'sdgfsdfg', 'gggg'))