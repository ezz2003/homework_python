# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

a = 4
b = 7
print(
    f"Плитка шоколада имеет размер {a} долек в ширину и {b} долек в высоту ломать можно 1 раз и только по прямой линии")
want_a_piece = int(input("Сколько долек вы хотите? "))

if want_a_piece == 0:
    message = "Вы очень скромный."
elif a*b == want_a_piece:
    message = "Это вся плитка, забирайте."
elif a*b < want_a_piece:
    message = "В этой плитке меньше долек, чем Вы желаете."
elif not (want_a_piece % a) or not (want_a_piece % b):
    message = "Возьмите, пожалуйста"
else:
    message = "Невозможно столько отломить."

print(message)
