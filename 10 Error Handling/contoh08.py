def cek_ketersediaan_dekorator(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                with open(file_name, 'r') as file:
                    isi = file.read()
                    return func(isi)
            except FileNotFoundError:
                print(f"Maaf, file tidak ditemukan.")
        return wrapper
    return decorator

@cek_ketersediaan_dekorator('nama_file.txt')
def pembaca_file():
    print("File ada")
