
class FileChecker:
    def __init__(self, file_name):
        self.file_name = file_name

    def cek_ketersediaan_file(self):
        try:
            with open(self.file_name, 'r') as file:
                isi = file.read()
                return isi,True
        except FileNotFoundError:
            return "Data Tidak Ada",False

def pembaca_file():
    file_checker = FileChecker('data.txt')
    (data, tersedia) = file_checker.cek_ketersediaan_file()
    print(data)

pembaca_file()