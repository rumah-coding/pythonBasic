# Sederhana 2: Menggunakan Try-Except untuk Mengecek File yang Tidak Ada
try:
    with open('data.txt', 'r') as file:
        isi = file.read()
        print(isi)
except FileNotFoundError:
    print("Maaf, file tidak ditemukan.")
