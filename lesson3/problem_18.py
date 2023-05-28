# Задача 18: Требуется найти в массиве A[1..N] самый близкий по # величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка # содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5


def find_closest_element(arr, num):
    i = 0
    while True:
        a = num + i
        b = num - i
        if a in l and b in l:
            return a, b
        elif a in l:
            return a, None
        elif b in l:
            return b, None
        i += 1


l = [1, 2, 3, 4, 5, 8, 10, 33, 63, 24, 18, 15, 13]
if not len(l):
    print("\nЭто пустой список! Мы ничего не найдём")
else:
    try:
        for k in l:
            k = int(k)
    except:
        print("\nВ списке есть не числовые значения. Возьмите другой список.")
    else:
        n = int(input("Введите число: "))
        if n in l:
            x, y = n, None
        else:
            x, y = find_closest_element(l, n)
        answer = f'и число {y}' if y else ''
        print(f'\nЧисло {x} {answer}')

