"""
Case : 1
Jika kita membuat daftar semua bilangan asli yang lebih kecil daripada 10
yang merupakan kelipatan 3 atau 5, maka kita akan mendapatkan 3, 5, 6, dan 9.
Jumlah dari bilangan-bilangan tersebut adalah 23.

Tentukanlah jumlah dari semua bilangan kelipatan 3 atau 5 yang lebih kecil daripada 1000.
"""
kelipatan3 = []
kelipatan5 = []
hasil = 0
for a in range(1, 1000):
    if (a % 3 == 0):
        kelipatan3.append(a)
for b in range(1, 1000):
    if (b % 5 == 0):
        kelipatan5.append(b)
gabungan = kelipatan3 + kelipatan5
listfinal = set(gabungan)
for x in listfinal:
    hasil += x
print(hasil)

sum_number = sum([n for n in range(1000) if n%3 == 0 or n%5 == 0])
print(sum_number)