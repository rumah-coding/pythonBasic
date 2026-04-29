import numpy as np
# Array 1D
nilai = np.array([85, 70, 92, 78, 88])
print(nilai.shape)      # (5,) — 5 elemen
print(nilai.dtype)      # int64

# Array 2D (seperti matriks)
matriks = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print(matriks.shape)    # (3, 3) — 3 baris, 3 kolom
print(matriks.dtype)    # int64