"""
Project Euler's Problem 014

Sebuah barisan iteratif berikut didefinisikan untuk himpunan bilangan bulat positif dengan aturan:
    n → n/2 (n ∈ bilangan genap)
    n → 3n + 1 (n ∈ bilangan ganjil)
Menggunakan aturan di atas, dimulai dari 13, maka kita akan mendapatkan barisan:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Dapat terlihat bahwa barisan ini (yang dimulai dari 13 dan berakhir di 1) memiliki 10 suku.
Meskipun belum ada bukti matematisnya, diperkirakan bahwa apapun bilangan awalnya, barisan
seperti ini akan selalu berakhir di 1 (Masalah Collatz).
Bilangan awal manakah yang besarnya lebih kecil daripada satu juta yang akan menghasilkan barisan terpanjang?

Catatan : besar suku berikutnya (setelah bilangan awal) dalam barisan boleh melebihi satu juta.
"""
from time import time
import psutil
t0 = time()
daftar_bilangan = [x for x in range(999999, 500000, -2)]
init = [0, 0]
for i in daftar_bilangan:
    temp = i
    suku = [i]
    while i != 1:
        if i % 2 == 0:
            i /= 2
            suku.append(i)
        else:
            i = 3*i + 1
            suku.append(i)
    if len(suku) > init[0]:
        init = [len(suku), temp]
print(init[1],"creates", init[0])
print("\nfinished in", time()-t0, "seconds")
print("takes",psutil.Process().memory_info().vms / 1024 ** 2,"MB of memory")