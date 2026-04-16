angka = [1, 2, 3]
angka_dibagi_2 = [x / 2 for x in angka]

print(angka_dibagi_2)  # Output: [0.5, 1.0, 1.5]

# Contoh List Comprehension dengan filter
data_mahasiswa = [
    {"nama": "Udin", "umur": 20},
    {"nama": "Dedi", "umur": 21},
    {"nama": "Asep", "umur": 22}
]
mahasiswa_dewasa = [x for x in data_mahasiswa if x["umur"] >= 21]

print(mahasiswa_dewasa)  # Output: [{'nama': 'Dedi', 'umur': 21}, {'nama': 'Asep', 'umur': 22}]

# Contoh List Comprehension dengan fungsi lambda
data_mahasiswa = [
    {"nama": "Udin", "umur": 20},
    {"nama": "Dedi", "umur": 21},
    {"nama": "Asep", "umur": 22}
]
mahasiswa_dewasa = [(x["nama"], x["umur"]) for x in data_mahasiswa if x["umur"] >= 21]

print(mahasiswa_dewasa)  # Output: [('Dedi', 21), ('Asep', 22)]

# Contoh List Comprehension dengan menggunakan enumerate
data_mahasiswa = [
    {"nama": "Udin", "umur": 20},
    {"nama": "Dedi", "umur": 21},
    {"nama": "Asep", "umur": 22}
]
mahasiswa_dewasa = [(x["nama"], i, x["umur"]) for i, x in enumerate(data_mahasiswa) if x["umur"] >= 21]

print(mahasiswa_dewasa)  # Output: [('Dedi', 1, 21), ('Asep', 2, 22)]

# Contoh List Comprehension dengan menggabungkan kondisi dan operasi
data_mahasiswa = [
    {"nama": "Udin", "umur": 20},
    {"nama": "Dedi", "umur": 21},
    {"nama": "Asep", "umur": 22}
]
mahasiswa_dewasa_atas_21 = [(x["nama"], x["umur"]) for i, x in enumerate(data_mahasiswa) if x["umur"] >= 21 and x["umur"] <= 22]

print(mahasiswa_dewasa_atas_21)  # Output: [('Dedi', 21)]

# Contoh List Comprehension dengan menggunakan dictionary comprehension
data_mahasiswa = [
    {"nama": "Udin", "umur": 20},
    {"nama": "Dedi", "umur": 21},
    {"nama": "Asep", "umur": 22}
]
mahasiswa_dewasa_atau_baik = {x["nama"]: x["umur"] for x in data_mahasiswa if x["umur"] >= 21 or x["umur"] <= 20}

print(mahasiswa_dewasa_atau_baik)  # Output: {'Udin': 20, 'Dedi': 21, 'Asep': 22}