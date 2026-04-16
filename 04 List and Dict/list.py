# Builtin Collection List

# List adalah sebuah type data yang dapat menampung banyak nilai, seperti array di bahasa lain.
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# List dapat menampung nilai-nilai apa pun, termasuk string dan boolean.
my_list = ["Hello", True, 123]
print(my_list)  # Output: ['Hello', True, 123]

# Anda dapat menambahkan nilai baru ke dalam list menggunakan operator += atau append().
my_list = [1, 2, 3]
my_list += [4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Anda dapat mengakses nilai-nilai dalam list menggunakan indeks.
my_list = [1, 2, 3]
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 3

# Anda dapat mengubah nilai-nilai dalam list menggunakan indeks.
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]

# Anda dapat menghapus nilai-nilai dalam list menggunakan indeks.
my_list = [1, 2, 3]
del my_list[0]
print(my_list)  # Output: [2, 3]

# Anda dapat looping melalui elemen-elemen dalam list menggunakan for loop.
my_list = [1, 2, 3]
for i in my_list:
    print(i)

# Berikut beberapa metode built-in yang umum digunakan pada list:
#   - len(): mengembalikan panjang list
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3

#   - min() dan max(): mengembalikan nilai terkecil atau terbesar dalam list
my_list = [10, 20, 30]
print(min(my_list))  # Output: 10
print(max(my_list))  # Output: 30

#   - sorted(): mengembalikan list yang telah diurutkan
my_list = [4, 2, 1, 3]
print(sorted(my_list))  # Output: [1, 2, 3, 4]

#   - reverse(): membalik urutan elemen-elemen dalam list
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

# Berikut beberapa fungsi built-in yang umum digunakan pada list:
#   - all(): mengembalikan True jika semua elemen dalam list adalah benar
my_list = [True, True, False]
print(all(my_list))  # Output: False

#   - any(): mengembalikan True jika salah satu elemen dalam list adalah benar
my_list = [False, False, True]
print(any(my_list))  # Output: True

# Berikut contoh penggunaan modul pada list:
import math
my_list = [1, 2, 3]
math.prod(my_list)  # Output: 6

print("Berikut adalah beberapa contoh penggunaan built-in function pada list:")