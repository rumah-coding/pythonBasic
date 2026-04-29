import numpy as np

matriks = np.array([
    [1, 2, 3],#mahasiswa A: UAS, UTS, Tugas
    [4, 5, 6],#mahasiswa B: UAS, UTS, Tugas
    [7, 8, 9]])#mahasiswa C: UAS, UTS, Tugas

print("Matriks Asli:")
print(matriks)
print("\nSlicing Baris 1:")
print(matriks[0])  # Baris pertama (indeks 0)

print(matriks[0, :])     # Baris 0 semua kolom: [85, 70, 92]
print(matriks[:,1])     # Baris 1 semua kolom: [78, 88, 90]
print(matriks[0:2, 1:])    # Baris 1, Kolom 2: 88
