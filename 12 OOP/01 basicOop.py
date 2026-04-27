class Mahasiswa:
    '''
    Kelas Mahasiswa untuk menyimpan data mahasiswa
    '''

    # class variable, shared by all instances of the class
    universitas = "Universitas Multimedia Nusantara"

    def __init__(self, nama, npm, ipk):
        '''
        Konstruktor - dipanggil otomatis saat objek dibuat.
        self adalah referensi ke objek yang sedang dibuat.
        '''
        self.nama = nama
        self.npm = npm
        self.ipk = ipk
        self.mataKuliah =["matematika", "fisika"]  # contoh daftar mata kuliah awal 

    def tambahMataKuliah(self, mataKuliah):
        '''
        Method untuk menambahkan mata kuliah ke daftar mata kuliah mahasiswa.
        '''
        self.mataKuliah.append(mataKuliah)
        print(f"{self.nama} terdaftar mata kuliah {mataKuliah}")

    def getPredikat(self):
        '''
        Mengembalikan predikat berdasarkan IPK mahasiswa.
        '''
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        else:
            return "Cukup"

    def __str__(self):
        '''
        Method khusus untuk mengembalikan representasi string dari objek.
        Dipanggil saat kita menggunakan print() pada objek.
        '''
        return f"Nama: {self.nama}, NPM: {self.npm}, IPK: {self.ipk}, Universitas: {Mahasiswa.universitas}" 

budi = Mahasiswa("Budi", "12345678", 3.6)
print(budi)  # Output: Nama: Budi, NPM: 12345678, IPK: 3.6, Universitas: Universitas Multimedia Nusantara
budi.tambahMataKuliah("Pemrograman Berorientasi Objek")  # Output: Budi terdaftar mata kuliah Pemrograman Berorientasi Objek
print(budi.getPredikat())  # Output: Cum Laude  
