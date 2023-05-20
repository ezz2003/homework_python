# Задача 2: Найдите сумму цифр трехзначного числа

number = input("Введите трёхзначное число:")

# только для трехзначного числа
number_int = int(number)
summ_int = number_int//100 + number_int//10 % 10 + number_int % 10

# для любого числа
summ_str = 0
for i in number:
    summ_str += int(i)

print(summ_int, summ_str)
