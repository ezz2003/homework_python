# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)


from random import randint


def find_indexes(arr, r_min, r_max):
    return [x for x in range(len(arr)) if r_min < arr[x] < r_max]


n = 15
range_min = -20
range_max = 20
array = [randint(-50, 50) for i in range(n)]
print(array)
print(find_indexes(array, range_min, range_max))
