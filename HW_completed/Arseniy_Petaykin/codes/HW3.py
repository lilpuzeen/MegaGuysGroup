# # 1 задание
# # № 16033
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r += "0"
#         r += "1"
#     else:
#         r += "1"
#         r += "0"
#     result = int(r,2)
#     if result > 102:
#         print(result)
#         break
#Ответ: 105
# # 2 задание
# # № 45239
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = "10" + r
#     else:
#         r = "1" + r + "01"
#     result = int(r,2)
#     if result > 441:
#         print(n)
#         break
# Ответ: 47
# # 3 задание
# # № 33750
# for n in range(2,1000):
#     r = bin(n)[2:]
#     r = r[:-1] + r[1] + r[1]
#     result = int(r,2)
#     if result > 76:
#         print(n)
#         break
# Ответ: 40
# # 4 Задание
# # № 33475
# for n in range(2,1000):
#     r = bin(n)[2:]
#     r = r + r[-2] + r[1]
#     result = int(r,2)
#     if result > 180:
#         print(n)
#         break
# Ответ: 46
# # 5 задание
# # № 14265
# for n in range(100,1000):
#     s = str(n)
#     perv = int(s[0]) + int(s[1])
#     vtor = int(s[1]) + int(s[2])
#     fst = (min(perv,vtor))
#     snd = (max(vtor,perv))
#     result = str(fst) + str(snd)
#     if result == "812":
#         print(n)
#         break
# Ответ: 175
# # 6 extra задание, обязательное к выполнению, иначе 0 баллов за ДЗ
# Гигиея. Фрагмент картины «Медицина» (Роспись потолка для Венского Университета)
# Ответ:Universität Wien