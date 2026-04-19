def cek_ketersediaan_generator(file_name):
    try:
        with open(file_name, 'r') as file:
            yield True
    except FileNotFoundError:
        yield False

def pembaca_file():
    generator = cek_ketersediaan_generator('nama_file.txt')
    if next(generator):
        print("File ada")
    else:
        print("File tidak ada")
