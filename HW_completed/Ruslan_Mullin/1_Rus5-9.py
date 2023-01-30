# 5зад
a = [1, 2, 4, 9, 10]
k = 0
for x in a:
    if x % 2 == 0:
        k = k + x
print(k)

#6зад
a = [1, 2, 4, 9, 10]
k = 0
for x in a:
    if x % 2 != 0:
        k = k + x
print(k)

#7зад
a = [1, 2, 4, 9, 10]
k = 0
for x in a:
    if x > 3:
        k = k + x
        print(k)

#8зад
a = [1, 2, 4, 9, 10]
k = 0
for x in a:
    if x < 3:
        k = k + x
        print(k)

#9зад
a = [1, 2, 4, 9, 10]
k = 0
for x in a:
    if x > 3 and x < 7:
        k = k + x
        print(k)