def pembaca_file():
    with open('nama_file.txt', 'r') as file:
        isi = file.read()
        print(isi)