import numpy as np  

zeroes = np.zeros((3, 4))  # Array 3x4 dengan semua elemen 0
ones = np.ones((2, 5))     # Array 2x5 dengan semua elemen 1
identitas = np.eye(4)     # Array 4x4 dengan elemen diagonal 1 dan lainnya 0    
acak = np.random.rand(3, 3)  # Array 3x3 dengan nilai acak antara 0 dan 1

print("Array Zeroes:\n", zeroes)
print("\nArray Ones:\n", ones)
print("\nArray Identitas:\n", identitas)    
print("\nArray Acak:\n", acak)  