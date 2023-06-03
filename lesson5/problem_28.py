# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.


def sum(a, b):
    if b == 0:
        return a
    a += 1
    return sum(a, b - 1)


n = 3
m = 5

print(sum(n, m))
print(sum(33, 66))