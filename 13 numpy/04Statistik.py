import numpy as np

nilai = np.array([10, 20, 30, 40, 50])
nilai = np.append(nilai, [60, 70, 80, 90, 100])  # Menambahkan nilai baru ke array
nilai = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

print("Nilai:", nilai)
print("Rata-rata:", np.mean(nilai))
print("Median:", np.median(nilai))
print("Variansi:", np.var(nilai))
print("Standar Deviasi:", np.std(nilai))
print("Minimum:", np.min(nilai))
print("Maximum:", np.max(nilai))
print("Persentil 25:", np.percentile(nilai, 25))
print("Persentil 50:", np.percentile(nilai, 50))
print('argmin:', np.argmin(nilai))
print('argmax:', np.argmax(nilai))