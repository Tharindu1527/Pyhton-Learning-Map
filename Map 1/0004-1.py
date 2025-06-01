limit = 100  # Maximum value
a, b = 0, 1

print("Fibonacci sequence up to", limit)
for _ in range(limit):
    if a > limit:
        break
    print(a, end=' ')
    a, b = b, a + b
