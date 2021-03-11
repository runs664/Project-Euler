"""
Project Euler's Problem 001

Jika kita membuat daftar semua bilangan asli yang lebih kecil daripada 10
yang merupakan kelipatan 3 atau 5, maka kita akan mendapatkan 3, 5, 6, dan 9.
Jumlah dari bilangan-bilangan tersebut adalah 23.

Tentukanlah jumlah dari semua bilangan kelipatan 3 atau 5 yang lebih kecil daripada 1000.
"""
#normal
jumlah = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        jumlah += i
print(jumlah)

#oneliner
total = sum([n for n in range(1000) if n%3 == 0 or n%5 == 0])
print(total)