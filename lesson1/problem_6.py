# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no
#

import os
os.system('cls')

# number = input('Введите номер билета')
number = 385916

if (number // 100000 + number % 100000 // 10000 + number % 10000 // 1000) == (number % 1000 // 100 + number % 100 // 10 + number % 10):
    print('Билетик съедобный.\n')
else:
    print("После поездки утилизируйте билет путём помещения его в мусорную корзину\n\n")

s_left = 0
s_right = 0
number_str = str(number)
for i, j in zip(number_str[:4], number_str[3:]):
    s_left += int(i)
    s_right += int(j)

if s_left == s_right:
    print('Подтверждено: "билет счастливый"\n')
else:
    print('Подтверждено: Билет можно утилизировать. \n')
