# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def pow(a, b):
    if b == 1:
        return a
    if b != 1:
        return (a * pow(a, b-1))
        

a = int(input('Enter A: '))
b = int(input('Enter B: '))


print(pow(a, b))