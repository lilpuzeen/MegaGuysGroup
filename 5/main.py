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

