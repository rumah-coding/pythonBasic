
# Sederhana 1: Menangani Salah Input Data
try:
    nama = input("Masukkan Nama Anda: ")
except ValueError:
    print("Maaf, nama tidak bisa diisi dengan angka.")
