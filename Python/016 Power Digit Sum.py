"""
Project Euler's Problem 016

2^15 = 32768 dan jumlah semua digitnya adalah 3 + 2 + 7 + 6 + 8 = 26.
Berapakah jumlah digit dari angka 2^1000?
"""
print(sum(int(n) for n in str(2**1000))) # i love this oneliner so much --> O(n)