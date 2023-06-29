# Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с 
# помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()


# input = 'a a a b c a a d c d d'
# list = input.split()
# list_2 = {}

# for i in range(len(list)):
#     if list[i] not in list_2.keys():
#         list_2[list[i]] = 0
#         print(f'{list[i]} ', end='')
#     else:
#         list_2[list[i]] += 1
#         print(f'{list[i]}_{list_2[list[i]]} ', end='')

# Пользователь вводит текст(строка). Словом считается последовательность 
# непробельных символов идущих подряд, 
# слова разделены одним пробелом. 
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# text_string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# print(text_string.split())
# print(len(set(text_string.lower().split())))

# print(text_string.isdigit())
# print(ord('a'), ord('z'))

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2  друга оказались не такими смышлеными. 
# Никто из ребят не смог до конца сделать это задание. 
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.

# n = int(input())
# maxx = n
# while n > 0:
#     n = int(input())
#     if maxx < n:
#         maxx = n
# print(maxx)

# или

# numbers = []   # создаем пустой список для хранения чисел
# while True:
#     num = int(input("Введите неотрицательное целое число (0 - для завершения ввода): "))
#     if num == 0:
#         break   # если введен 0, то прерываем цикл
#     numbers.append(num)   # добавляем число в список
# if numbers:   # если список не пустой
#     print("Наибольший элемент последовательности, который завершается первым встретившимся нулем:", max(numbers))
# else:
#     print("Последовательность пуста.")

# Моржовый оператор:
# while (n:= int(input('--> '))) < 0:
#     print('Мало')