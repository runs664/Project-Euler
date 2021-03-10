""" 
Project Euler's Problem 004

Sebuah bilangan disebut sebagai palindrom, bila kita membacanya baik dari depan maupun dari
belakang, kita akan mendapatkan bilangan yang sama.
Bilangan palindrom terbesar hasil dari perkalian dua buah bilangan 2 digit adalah 9009 = 91 × 99.
Tentukan bilangan palindrom terbesar hasil dari perkalian dua buah bilangan 3 digit.
"""
palindrom = []
for x in range(100, 1000):
    for y in range(100, 1000):
        n = x * y
        m = str(n)
        if m == m[::-1]:
            palindrom.append(n)
hasil = list(sorted(set(palindrom)))
print(hasil[-1])