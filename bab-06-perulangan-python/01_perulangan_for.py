x = 9
y = 1
print("x =", x)
print("y =", y)

print("=== Bilangan 1 sampai 12 + x ===")
for i in range(1, 12 + x + 1):
    print(i)

print("=== Kelipatan 3 sebanyak 5 + y ===")
for i in range(3, 3 * (5 + y) + 1, 3):
    print(i)

print("=== Hitung mundur dari 12 + x ===")
for i in range(12 + x, 0, -1):
    print(i)