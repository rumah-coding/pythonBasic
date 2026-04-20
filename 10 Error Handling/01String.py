
try:
    nama = input("Masukkan Nama Anda: ")
    int(nama )
    print("Maaf, nama tidak bisa diisi dengan angka.")

except ValueError:
    print("Haloo, " + nama + "! Selamat datang di dunia Python.")
