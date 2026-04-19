
class FileChecker:
    def __init__(self, file_name):
        self.file_name = file_name

    def cek_ketersediaan_file(self):
        try:
            with open(self.file_name, 'r') as file:
                isi = file.read()
                return True
        except FileNotFoundError:
            return False

def pembaca_file():
    file_checker = FileChecker('nama_file.txt')
    if file_checker.cek_ketersediaan_file():
        print("File ada")
    else:
        print("File tidak ada")
