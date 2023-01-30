# # Задание 1 (№39663)
# arr = [int(x) for x in open('39763.txt')]
# counter = 0
# maxx = float('-inf')
# for i in range (len(arr) - 2):
#     a = arr[i]
#     b = arr[i + 1]
#     c = arr[i + 2]
#     summ = a + b + c
#     if (a**2 < (b**2 + c**2)) and (b**2 < (a**2 + c**2)) and (c**2 < (b**2 + a**2)):
#         counter += 1
#         maxx = max(summ,maxx)
# print(counter,maxx)
# Ответ : 1175 29451
# # Задание 2 (№37344)
# arr = [int(x) for x in open ('37344.txt')]
# counter = 0
# maxx = float('-inf')
# for i in range(len(arr) - 1):
#     for j in range(i + 1,len(arr)):
#         a = arr[i]
#         b = arr[j]
#         if (a * b) % 10 == 0:
#             counter += 1
#             maxx = max(maxx, a + b)
# print(counter,maxx)
# Ответ: 13510315 19999 (минус пк :( )
# Задание 3 (№37354)
# arr = [int(x) for x in open ('37354.txt')]
# counter = 0
# maxx = float('-inf')
# for i in range(len(arr) - 1):
#     for j in range(i + 1,len(arr)):
#         a = arr[i]
#         b = arr[j]
#         if (a + b) % 2 == 1 and (a * b) % 5 == 0:
#             counter += 1
#             maxx = max(maxx, a + b)
# print(counter,maxx)
# Ответ: 9082691 19995
# # Задание 4 (№47221)
# arr = [int(x) for x in open ('47221.txt')]
# counter = 0
# maxx = float('-inf')
# maximum = max(list(filter(lambda x: x % 10 == 3, arr)))
# for i in range(len(arr) - 1):
#     a = arr[i]
#     b = arr[i + 1]
#     a3 = str(a)
#     b3 = str(b)
#     if ((a3[-1] == '3') and (b3[-1] != '3') or (a3[-1] != '3') and (b3[-1] == '3')) and (maximum**2) <= (a**2 + b**2):
#         counter += 1
#         maxx = max(maxx, a**2 + b**2)
# print(counter,maxx)
# Ответ:180 190360573
# Extra задание
# Задание: Shoes
# Ответ: 315123-030