"""
Project Euler's Problem 015

Jika kita mulai bergerak dari pojok kiri atas kisi berukuran 2×2, dan hanya boleh bergerak ke
kanan atau ke bawah, maka akan ada persis 6 ruas rute menuju ke pojok kanan bawah.
Berapakah jumlah rute yang ada jika kisi berukuran 20×20?
"""
# proggramming approach
from time import time
import psutil
def countRoutes():
    #x = int(input("Masukkan X grid: "))
    #y = int(input("Masukkan Y grid: "))
    x = 20
    y = 20
    t0 = time()
    lst= list(range(1,x+2))
    while lst[1]!=y+1:
        i=0
        for n in lst[1:]:
            i+=1
            lst[i]=n+lst[i-1]
    print(f"Ada {lst[-1]} rute dalam {x}x{y} grid!")
    print("\nfinished in =", time()-t0)
    print("takes",psutil.Process().memory_info().vms / 1024 ** 2,"MB of memory")
countRoutes()

# mathematical approach --> untuk 2x2 diperlukan 4 langkah, kombinasi 4 dari 2 adalah 6, maka 20x20 diperlukan 40 langkah:
from math import factorial
print(int(factorial(40)/(factorial(20)*factorial(20))), "--> with factorial") # kombinasi 40 dari 20