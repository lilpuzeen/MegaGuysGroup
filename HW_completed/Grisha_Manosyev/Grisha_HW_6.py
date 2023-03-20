# Салам уебки! Сегодня порешаем 16-ые задачки.
# Помимо новых задачек, закину еще парочку для повторения (вы сами просили)


# Задание 1
# 5245 (№16 в ЕГЭ)
# def f(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return 3*f(n - 1) - 2*f(n - 2)
# print(f(7))
# Задание 2
# 4657 (№16 в ЕГЭ)
# def f(n):
#     if n == 1:
#         return 1
#     return 2*g(n - 1) + 5*n
# def g(n):
#     if n == 1:
#         return 1
#     return f(n - 1) + 2*n
# print(f(4) + g(4))
# Задание 3
# 33504 (№2 в ЕГЭ)
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x == (not(y))) <= (y and (not(z))) or (z and (not(w)))) == 0:
#                     print(x, y, z, w, '0')
# answer:wzxy
# Задание 4
# 28542 (№5 в ЕГЭ)
# def calc(x, a, b):
#     s = ''
#     x = int(str(x), a)
#     while x > 0:
#         s += str(x % b)
#         x //= b
#     return s[::-1]
# for n in range(1000):
#     r = calc(n, 10, 3)
#     r += str(n % 3)
#     r = int(r, 3)
#     if r > 1000:
#         print(r)
# answer: 1003
# Задание 5
# 37371 (№17 в ЕГЭ)
# count = 0
# maxx = float('-inf')
# arr = [int(x) for x in open('service_files/37371.txt')]
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         a = arr[i]
#         b = arr[j]
#         if (a - b) % 60 == 0:
#             count += 1
#             maxx = max(maxx, a - b)
# print(count, maxx)
# answer: 832722 9960

# Extra задание
# Напишите рекурсивный вариант бинарного поиска (поиск элемента в отсортированном массиве)
# Внимательно изучите работу бинарного поиска, чтобы понять как его реализовать
# Я понимаю что скорее всего вы скатаете, но мне пиздец как важно чтоб вы поняли этот алгоритм.
# Это самая база. Прям базовее некуда. Потрените еще заодно понимание рекурсии)))
# Dear Arman. I apologize. I don't have time to do this part of task. Could you explain it to us?