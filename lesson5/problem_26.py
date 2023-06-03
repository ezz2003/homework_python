# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponentiation(a, b):
    if b == 0:
        return 1
    return a * exponentiation(a, b - 1)


n = 3
m = 5

print(exponentiation(n, m))
print(exponentiation(2, 3))
