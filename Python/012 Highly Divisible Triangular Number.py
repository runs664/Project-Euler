"""
Project Euler's Problem 012

Barisan bilangan segitiga dibuat dengan menjumlahkan bilangan asli. Maka bilangan segitiga ke-7
adalah 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Sepuluh bilangan segitiga pertama adalah:
            1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Jika kita membuat daftar faktor dari tujuh bilangan segitiga pertama:
    1 : 1
    3 : 1,3
    6 : 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
Dapat terlihat bahwa 28 adalah bilangan segitiga pertama yang memiliki lebih dari lima faktor.
Berapakah bilangan segitiga pertama yang memiliki lebih dari lima ratus faktor?
"""
from functools import reduce
import time

# brute force --VERY SLOW-- (berjam-jam mungkin)
""" def bilangan_segitiga(n):
    hasil = 0
    for i in range(1, n+1):
        hasil += i
    return hasil

j = 1
hasil = 0
while True:
    faktor = sorted(set(reduce(list.__add__,([i, bilangan_segitiga(j)//i] for i in range(1, int(bilangan_segitiga(j)**0.5) + 1) if bilangan_segitiga(j) % i == 0))))
    if len(faktor) > 500:
        hasil = j
        break
    j += 1
    print(j, len(faktor))
print(hasil) """

# optimized algorithm
t0 = time.time()
n = 28
while True:
    triangle_number = n*(n+1)/2
    n += 1
    dic = {}
    i = 2
    while i <= triangle_number:
        if triangle_number % i == 0:
            triangle_number = triangle_number/i
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            i -= 1
        i += 1

    powers = map(lambda x:(x+1), dic.values())
    divisors = reduce(lambda x,y:x*y, powers)
    if divisors > 500:
        print((n-1)*(n)/2)
        break

print(time.time()-t0)