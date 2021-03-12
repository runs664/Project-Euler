"""
Project Euler's Problem 010

Jumlah semua bilangan prima yang lebih kecil daripada 10 adalah 2 + 3 + 5 + 7 = 17.
Tentukanlah jumlah semua bilangan prima yang lebih kecil dari dua juta (2 000 000).
"""
import time, math
hasil = 0
daftar = []
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n%i == 0:
            return False
    return True

t0 = time.time()
for n in range(1, 2000000):
    if is_prime(n) == True:
        daftar.append(n)
for x in daftar:
    hasil += x
print(hasil)
print('Operation completed in', round(time.time() - t0, 6), 'second')