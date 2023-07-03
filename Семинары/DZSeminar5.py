# Напишите программу, которая на вход принимает два числа A и B, 
# возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# def exponentiation(n,m):
#     if m == 0:
#         return 1
#     if n == 0:
#         return 1
#     return exponentiation(n, m-1)*n

# num_A = int(input())
# num_B = int(input())
# result = exponentiation(num_A, num_B)
# print(result) 

# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

# def amount(n,m):
#     if m == 0:
#         return n
#     if n == 0:
#         return m
#     return amount(n, m-1)+1

# num_A = int(input())
# num_B = int(input())
# result = amount(num_A, num_B)
# print(result) 