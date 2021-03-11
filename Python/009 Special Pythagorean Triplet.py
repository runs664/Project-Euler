"""
Project Euler's Problem 009

Triplet Pythagoras adalah kumpulan tiga buah bilangan asli, a < b < c, yang memenuhi,
                                    a^2 + b^2 = c^2
Sebagai contoh, 3^2 + 4^2 = 9 + 16 = 25 = 5^2 .
Dan hanya terdapat persis satu triplet Pythagoras yang bisa memenuhi a + b + c = 1000. Temukan
triplet Pythagoras tersebut dan tentukanlah hasil a × b × c.
"""
import time
s = time.time()
hasil = 0
for x in range(1, 1001):
    for y in range(1, 1001):
        z = 1000 - (x + y)
        if (x**2 + y**2) == z**2:
            bil = "{}, {}, {}".format(x,y,z)
            hasil = x*y*z
            break
print(hasil,"from",bil)
print('Operation completed in', round(time.time() - s, 6), 'second')