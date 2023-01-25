# print("I made homework! Yay! I'm gay!") Okay man<3
# Салам бездари! Рад вас снова тут видеть!
# * Сегодня решаем 17-ые задачи и extra задачу на умение гуглить!
# * Extra задача не является обязательной к выполнению, но по мне она крайне интересная и советую вам посидеть над ней
# * Если возникнут затруднения, обращайтесь за подсказкой
#
# Также хочу вас обрадовать, что эта домашка станет нашей отправной точкой в мир GitHub!
# * Отныне, начиная с этого задания, решения ДЗ вы будете "пушить" в наш репозиторий
# * Подробная инструкция, будет чуть позже выложена в общий чат
# * По всем вопросам касательно работы с GitHub обращайтесь ко мне или гуглите)
# ** Всех обнял! **
#
# Доп. инстуркция к выполнению этой домашки.
# * Все текстовые файлы прошу называть номером задачи из РешуЕГЭ.
# * Переделайте свою папку так, чтобы в ней было легко разобраться, -
# - и нельзя было потеряться среди файлов домашек и файлов требуемых к выполнению задания
#
#
# 1 задание
# 39763
# arr = [int(x) for x in open('39763.txt')]
# count = 0
# maxx = float('-inf')
# for i in range(len(arr) - 2):
#     a = arr[i]
#     b = arr[i + 1]
#     c = arr[i + 2]
#     if ((a**2 + b**2) > c**2) and ((a**2 + c**2) > b**2)  and ((b**2 + c**2) > a**2):
#         count += 1
#         maxx = max(maxx, a + b +c)
# print(count, maxx)

# 2 задание
# 37344
# arr = [int(x) for x in open('37344.txt')]
# count = 0
# maxx = float('-inf')
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         a = arr[i]
#         b = arr[j]
#         if ((a*b) % 10 == 0):
#             count += 1
#             maxx = (max(maxx, (a + b)))
# print(count, maxx)


# 3 задание
# 37354
# arr = [int(x) for x in open('37354.txt')]
# count = 0
# maxx = float('-inf')
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         a = arr[i]
#         b = arr[j]
#         if ((a + b) % 2 != 0) and ((a*b) % 5 == 0):
#             count += 1
#             maxx = max(maxx, a + b)
# print(count, maxx)


# 4 задание
# 47221
# arr = [int(x) for x in open('47221.txt')]
# count = 0
# maxx = float('-inf')
# maximal =  max(list(filter(lambda x: x % 10 == 3, arr)))
# for i in range(len(arr) - 1):
#         a = arr[i]
#         b = arr[i + 1]
#         if (((str(a)[-1] == '3') and (str(b)[-1] != '3')) or ((str(b)[-1] == '3') and (str(a)[-1] != '3'))) and ((a**2 + b**2) >= (maximal**2)):
#             count += 1
#             maxx = max(maxx, a**2 + b**2)
# print(count, maxx)
#


# Extra задание
# Задание: Shoes
# Вам дана картинка по ссылке из файлообменика. Будьте добры, дать ответ на вопрос =>
# Что за кроссовки на нём надеты? В ответе нужно указать артикул товара согласно используемой производителем номенклатуре.

# My answer:
# If I'm not mistaken 315123-030
# https://dropmefiles.com/EYbZC