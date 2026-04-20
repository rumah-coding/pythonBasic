def cek_ketersediaan_generator(file_name):
    try:
        with open(file_name, 'r') as file:
            for baris in file:
                yield baris
    except FileNotFoundError:
        yield 'File tidak ditemukan'
    except Exception as e:
        yield f'Error: {str(e)}'

def pembaca_file():
    generator = cek_ketersediaan_generator('data.txt')
    # print(next(generator))  # Output: File tidak ditemukan
    for baris in generator:
        print(baris)

pembaca_file()