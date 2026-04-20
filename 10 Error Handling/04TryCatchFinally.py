def pembaca_file():
    try:
        with open('data.txt', 'r') as file:
            isi = file.read()
            return isi
    except FileNotFoundError as e:
        print(f"Maaf, file tidak ditemukan. {str(e)}")
    finally:
        print("Selesai membaca file!")
print(pembaca_file())   