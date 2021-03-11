""" 
Project Euler's Problem 007

Bila kita membuat daftar enam bilangan prima pertama: 2, 3, 5, 7, 11, dan 13, kita dapat melihat
bahwa bilangan prima ke-6 adalah 13.
Berapakah bilangan prima ke-10001?
"""
import time
s = time.time()
prima = [2, 3, 5, 7, 11, 13]
i = 14
while len(prima) < 10001:
    for j in prima:
        if i % j == 0:
            break
    else:
        prima.append(i)
    i+=1
# ini termasuk metode brute force juga
print(prima[-1])
print('Operation completed in', round(time.time() - s, 2), 'second')