# Contoh Program Sederhana Menggunakan JSON

import json

# Membuat Data dalam Format JSON
data = {
    "nama": "John Doe",
    "umur": 30,
    "alamat": {
        "jalan": "Jl. Raya No. 123",
        "kota": "Jakarta"
    }
}

# Mengubah Data ke Format JSON
json_data = json.dumps(data, indent=4)

print("Data dalam Format JSON:")
print(json_data)

# Membaca File JSON Sederhana
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Membuat File JSON yang Lebih Rumit dengan Menggunakan Objek Python
class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

mhs = Mahasiswa("Budi", 25)
mhs.alamat = {
    "jalan": "Jl. Raya No. 123",
    "kota": "Bandung"
}

# Mengubah Objek Python ke Format JSON dengan Menggunakan json.dumps
json_mhs = json.dumps(mhs.__dict__, indent=4)

print("Data dalam Format JSON:")
print(json_mhs)

# Membaca File JSON yang Lebih Rumit
with open('mhs.json', 'w') as file:
    json.dump(mhs.__dict__, file, indent=4)