""" 
Project Euler's Problem 003

Faktor prima dari 13195 adalah 5, 7, 13, dan 29.
Berapakah faktor prima terbesar dari bilangan 600851475143 ?
"""
from functools import reduce
n = 600851475143
faktor = sorted(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
prima = []
for i in faktor:
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        prima.append(i)
print(prima[-1])