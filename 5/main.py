# bin -> 2CC
# oct -> 8CC
# hex -> 16CC
# n *= s  <=> n = n * s
# n /= s  <=> n = n / s
# n %= s  <=> n = n % s
# n **= s  <=> n = n ** s
# n //= s  <=> n = n // s

# 8094
# for n in range(1, 100000):
# 	r = bin(n)[2:]
# 	r += str(r.count("1") % 2)
# 	r += str(r.count("1") % 2)
# 	if int(r, 2) > 43:
# 		print(int(r, 2))

# №27535 (№5 в ЕГЭ) (простое)
# for N in range(2, 1000):
#     R = bin(N)[2:]
#     R = R + R[1] + R[0]
#     R = int(R, 2)
#     if R > 90:
#         print(N)
#         break

# 47209
# for n in range(1, 1000):
# 	r = bin(n)[2:]
# 	digits = list(r)
# 	if digits.count("1") % 2 == 0:
# 		digits.append("0")
# 		digits[0], digits[1] = "1", "0"
# 	elif digits.count("1") % 2 != 0:
# 		digits.append("1")
# 		digits[0], digits[1] = "1", "1"
# 	result = int("".join(digits), 2)
# 	if result > 40:
# 		print(n)
# 		break

# 47209 2nd
# for n in range(1, 1000):
# 	r = bin(n)[2:]
# 	if r.count("1") % 2 == 0:
# 		r = "10" + r[2:] + "0"
# 	elif r.count("1") % 2 != 0:
# 		r = "11" + r[2:] + "1"
# 	result = int(r, 2)
# 	if result > 40:
# 		print(n)
# 		break
