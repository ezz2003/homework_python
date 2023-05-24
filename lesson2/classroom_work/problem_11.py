# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

def sequence_number_fibonacci(num):
    pre_v = 0
    nex_t = 1
    i = 3
    while nex_t < num:
        nex_t, pre_v = pre_v + nex_t, nex_t
        if nex_t == num:
            return i
        i += 1
    return -1


digit = 5
print(sequence_number_fibonacci(digit))
