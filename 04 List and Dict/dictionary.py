# Membuat dictionary sederhana
dict_sederhana = {'nama': 'Budi', 'umur': 20}

# Menambahkan elemen ke dalam dictionary
dict_sederhana['pekerjaan'] = 'Pegawai Negeri'

# Mengakses nilai dari dictionary
print(dict_sederhana['nama'])  # Output: Budi

# Mengubah nilai di dalam dictionary
dict_sederhana['umur'] = 25
print(dict_sederhana)  # Output: {'nama': 'Budi', 'umur': 25, 'pekerjaan': 'Pegawai Negeri'}

# Menghapus elemen dari dictionary
del dict_sederhana['pekerjaan']
print(dict_sederhana)  # Output: {'nama': 'Budi', 'umur': 25}

# Membuat dictionary dengan lebih banyak atribut
dict_lebih_banyak_atribut = {
    'nama': 'Budi',
    'umur': 20,
    'pekerjaan': 'Pegawai Negeri',
    'alamat': 'Jl. Sukmajaya, Kecamatan Jakarta Selatan'
}

# Membuat dictionary dengan menggunakan fungsi
def buat_dict(nama, umur):
    return {'nama': nama, 'umur': umur}

dict_dengan_fungsi = buat_dict('Budi', 20)
print(dict_dengan_fungsi)  # Output: {'nama': 'Budi', 'umur': 20}

# Membuat dictionary dengan menggunakan perulangan
def buat_dict_perulangan(nama, umur):
    dictnya = {}
    for i in range(5):
        dictnya[f'nilai_{i}'] = f'{nama}_nilai_{i}'
    return dictnya

dict_dengan_perulangan = buat_dict_perulangan('Budi', 20)
print(dict_dengan_perulangan)
# Output: {'nilai_0': 'Budi_nilai_0', 'nilai_1': 'Budi_nilai_1',
           #   'nilai_2': 'Budi_nilai_2', 'nilai_3': 'Budi_nilai_3',
           #   'nilai_4': 'Budi_nilai_4'}

# Membuat dictionary dengan menggunakan fungsi lambda
dict_dengan_lambda = {'nama': 'Budi', 'umur': 20}
dict_dengan_lambda['pekerjaan'] = lambda: print('Saya seorang pegawai negeri')
print(dict_dengan_lambda['pekerjaan']())  # Output: Saya seorang pegawai negeri

# Membuat dictionary dengan menggunakan ekspresi dictionary
dict_dengan_ekspresi_dict = {'nama': 'Budi', 'umur': 20, **{'pekerjaan': 'Pegawai Negeri'}}
print(dict_dengan_ekspresi_dict)
# Output: {'nama': 'Budi', 'umur': 20, 'pekerjaan': 'Pegawai Negeri'}

# Membuat dictionary dengan menggunakan fungsi yang mengembalikan dictionary
def buat_dict_mengembalikan():
    return {'nama': 'Budi', 'umur': 20}

dict_dengan_fungsi_mengembalikan = buat_dict_mengembalikan()
print(dict_dengan_fungsi_mengembalikan)
# Output: {'nama': 'Budi', 'umur': 20}