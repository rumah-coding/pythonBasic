def pembaca_file():
    with open('data.txt', 'r') as file:
        isi = file.read()
        print(isi)
pembaca_file()