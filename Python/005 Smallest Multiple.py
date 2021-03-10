""" 
Project Euler's Problem 005

2520 adalah bilangan terkecil yang dapat habis dibagi oleh semua angka dari 1 sampai 10.
Berapakah bilangan positif terkecil yang dapat habis dibagi oleh semua bilangan dari 1 sampai 20?
"""
i = 9699690 # merupakan hasil perkalian dari seluruh faktor prima antara 1 - 20, karena pasti lebih besar dari ini
while True:
    for x in range(1, 21):
        if i % x != 0:
            break
    else:
        print(i)
        break
    i += 1
# PS: Ini model pencarian secara brute force, sehingga memerlukan waktu cukup lama (+- 2 menit)