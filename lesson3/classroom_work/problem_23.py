# Задача №23. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


l = [0, -1, 5, 2, 3]

answer = []
for i in range(len(l)-1):
    if l[i] < l[i + 1]:
        answer.append(f'{l[i]} < {l[i + 1]}')

print(f'{len(answer)} ({", ".join(answer)})')
