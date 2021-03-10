""" 
Project Euler's Problem 006

Jumlah dari kuadrat sepuluh bilangan asli pertama adalah,
1 ^ 2 + 2 ^ 2 + ... + 10 ^ 2 = 385
Kuadrat dari jumlah sepuluh bilangan asli pertama adalah,
(1 + 2 + ... + 10) ^ 2 = 55 ^ 2 = 3025
Selisih antara jumlah dari kuadrat dengan kuadrat dari jumlah sepuluh bilangan asli pertama adalah 3025 - 385 = 2640.
Tentukan selisih antara jumlah dari kuadrat dengan kuadrat dari jumlah seratus bilangan asli pertama.
"""
jumlahkuadrat = kuadratjumlah = temp = 0
for i in range(1, 101):
    jumlahkuadrat += i**2
for j in range(1, 101):
    temp += j
    kuadratjumlah = temp**2
hasil = kuadratjumlah - jumlahkuadrat
print(hasil)