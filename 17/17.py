# # 37336
# arr = [int(x) for x in open("37336.txt")]
# count = 0
# # maxx = -10000000000000
# maxx = float("-inf")
# for i in range(len(arr) - 1):
# 	a = arr[i]
# 	b = arr[i + 1]
# 	if (a % 3 == 0) or (b % 3 == 0):
# 		count += 1
# 		maxx = max(maxx, a + b)
# print(count, maxx)

# # 37337
# arr = [int(x) for x in open("37337.txt")]
# count = 0
# maxx = float("-inf")
# for i in range(len(arr)):
# 	for j in range(i + 1, len(arr)):
# 		a = arr[i]
# 		b = arr[j]
# 		if ((a % 160) != (b % 160)) and ((a % 7 == 0) or (b % 7 == 0)):
# 			count += 1
# 			maxx = max(maxx, a + b)
# print(count, maxx)

# arr = [int(x) for x in open("37357.txt")]
# count = 0
# maxx = float("-inf")
# for i in range(len(arr)):
# 	for j in range(i + 1, len(arr)):
# 		a = arr[i]
# 		b = arr[j]
# 		if (a + b) % 8 == 0:
# 			count += 1
# 			maxx = max(maxx, a + b)
# print(count, maxx)
