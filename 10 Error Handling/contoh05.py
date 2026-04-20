def cek_ketersediaan_file(file_name):
    try:
        with open(file_name, 'r') as file:
            isi = file.read()
            return isi,True
    except FileNotFoundError:
        return 'Tidak Ada Data',False

def pembaca_file():
    (data, tersedia) = cek_ketersediaan_file('data.txt')
    print(data) 
pembaca_file()
