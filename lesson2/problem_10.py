# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть


coin_sides = "10110"

heads = 0
tails = 0
for i in coin_sides:
    if int(i):
        tails += 1
    else:
        heads += 1
print(f'\n Достаточно перевернуть {heads if tails > heads else tails} монеты')

side = 0
for i in coin_sides:
    side += int(i)
print(f'\n Совершенно верно: всего {side if side<len(coin_sides)/2 else len(coin_sides)-side} монеты')

