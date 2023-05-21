# Задача 2: Найдите сумму цифр трехзначного числа

import os
os.system('cls')

number = input("\n Введите трёхзначное число:")

# только для трехзначного числа
number_int = int(number)
summ_int = number_int//100 + number_int//10 % 10 + number_int % 10

# для любого числа
summ_str = 0
for i in number:
    summ_str += int(i)

print(
    f'\n сумма цифр числа (1 метод) = {summ_int}, сумма цифр числа (2 метод) = {summ_str}\n')
