# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

mess = ''
s = int(input("Введите количество журавликов: "))

s_true = s // 6 * 6
diff = s - s_true
if diff:
    mess = f"не проданы вчера - {diff}"

s_p = s_true / 6
s_s = s_p
s_k = (s_p + s_s) * 2


print(
    f'В наличии {int(s)} Изготовлено {s_true}  Катя {int(s_k)}, Петя {int(s_p)}, Серёжа {int(s_s)} {mess}')
