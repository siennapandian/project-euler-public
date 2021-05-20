
k = 1000
n = 1
total = 0
while n <= k:
    if n % 3 == 0 or n % 5 == 0:
        total += n
    n += 1
print(total)
