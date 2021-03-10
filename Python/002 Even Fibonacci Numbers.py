""" 
Project Euler's Problem 002

Setiap pola baru dalam barisan Fibonacci dibentuk dengan menjumlahkan dua buah bilangan sebelumnya.
Jika kita memulai barisan dengan angka 1 dan 2, maka 10 bilangan pertama barisan Fibonacci adalah:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Tentukanlah hasil penjumlahan semua bilangan genap yang lebih kecil dari empat juta dalam barisan Fibonacci seperti di atas. 
"""
n1 = 1
n2 = 2
nu = 0
fibonacci = [1, 2]
while True:
    x = n1
    y = n2
    nu = x + y
    if nu < 4000000:
        fibonacci.append(nu)
    else:
        break
    n1 = n2
    n2 = nu

hasil = sum(x for x in fibonacci if (x % 2 == 0))
print(hasil)