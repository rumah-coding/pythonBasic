def cek_ketersediaan_file(file_name):
    try:
        with open(file_name, 'r') as file:
            isi = file.read()
            return True
    except FileNotFoundError:
        return False

def pembaca_file():
    if cek_ketersediaan_file('nama_file.txt'):
        print("File ada")
    else:
        print("File tidak ada")

