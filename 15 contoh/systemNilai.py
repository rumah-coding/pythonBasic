"""
system_nilai.py
---------------
Sistem analisis nilai mahasiswa sederhana.
Mendemonstrasikan: OOP, Pandas, NumPy, File I/O, dan fungsi.

"""

import pandas as pd
import numpy as np
from pathlib import Path


# ============================================================
# BAGIAN 1: DEFINISI KELAS
# ============================================================

class AnalisNilai:
    """
    Kelas untuk menganalisis nilai mahasiswa dari file CSV.
    
    Contoh penggunaan:
        analis = AnalisNilai("nilai_mahasiswa.csv")
        analis.hitung_nilai_akhir()
        analis.tampilkan_statistik()
        analis.ekspor_hasil("hasil_analisis.csv")
    """
    
    # Bobot penilaian — class variable
    BOBOT = {
        "tugas": 0.20,
        "uts": 0.35,
        "uas": 0.45
    }
    
    def __init__(self, path_file: str):
        """
        Inisialisasi dengan membaca file CSV.
        
        Args:
            path_file: path ke file CSV berisi data nilai
        """
        self.path_file = Path(path_file)
        self.df = None
        self.__muat_data()
    
    def __muat_data(self):
        """
        Method private (konvensi: diawali _) untuk memuat data.
        Private berarti hanya dipakai di dalam kelas ini.
        """
        if not self.path_file.exists():
            raise FileNotFoundError(f"File tidak ditemukan: {self.path_file}")
        
        self.df = pd.read_csv(self.path_file)
        print(f"✅ Data berhasil dimuat: {len(self.df)} mahasiswa")
        
        # Validasi kolom yang wajib ada
        kolom_wajib = ["nama", "npm", "tugas", "uts", "uas"]
        kolom_hilang = [k for k in kolom_wajib if k not in self.df.columns]
        
        if kolom_hilang:
            raise ValueError(f"Kolom berikut tidak ditemukan: {kolom_hilang}")
    
    def hitung_nilai_akhir(self):
        """
        Menghitung nilai akhir berdasarkan bobot yang sudah ditentukan.
        Menambahkan kolom: nilai_akhir, predikat, lulus.
        """
        # Hitung nilai akhir dengan bobot
        self.df["nilai_akhir"] = (
            self.df["tugas"] * self.BOBOT["tugas"] +
            self.df["uts"]   * self.BOBOT["uts"]   +
            self.df["uas"]   * self.BOBOT["uas"]
        ).round(2)
        
        # Tentukan predikat menggunakan np.select (efisien untuk kondisi berlapis)
        kondisi = [
            self.df["nilai_akhir"] >= 85,
            self.df["nilai_akhir"] >= 75,
            self.df["nilai_akhir"] >= 60,
        ]
        pilihan = ["A", "B", "C"]
        self.df["predikat"] = np.select(kondisi, pilihan, default="D")
        
        # Tentukan status lulus
        self.df["lulus"] = self.df["nilai_akhir"] >= 60
        
        print("✅ Nilai akhir berhasil dihitung")
        return self  # mengembalikan self agar bisa chaining method
    
    def tampilkan_statistik(self):
        """Menampilkan ringkasan statistik ke terminal."""
        if "nilai_akhir" not in self.df.columns:
            print("⚠️  Jalankan hitung_nilai_akhir() terlebih dahulu")
            return self
        
        total = len(self.df)
        lulus = self.df["lulus"].sum()
        tidak_lulus = total - lulus
        
        print("\n" + "="*50)
        print("📊 STATISTIK NILAI MAHASISWA")
        print("="*50)
        print(f"Total mahasiswa : {total}")
        print(f"Lulus           : {lulus} ({lulus/total*100:.1f}%)")
        print(f"Tidak lulus     : {tidak_lulus} ({tidak_lulus/total*100:.1f}%)")
        print(f"\nRata-rata nilai akhir : {self.df['nilai_akhir'].mean():.2f}")
        print(f"Nilai tertinggi       : {self.df['nilai_akhir'].max():.2f}")
        print(f"Nilai terendah        : {self.df['nilai_akhir'].min():.2f}")
        
        print("\nDistribusi Predikat:")
        distribusi = self.df["predikat"].value_counts().sort_index()
        for predikat, jumlah in distribusi.items():
            bar = "█" * jumlah
            print(f"  {predikat}: {bar} ({jumlah} mahasiswa)")
        
        print("="*50)
        return self
    
    def ekspor_hasil(self, path_output: str):
        """
        Mengekspor hasil analisis ke file CSV.
        
        Args:
            path_output: path file output
        """
        path = Path(path_output)
        print(f'path = {path}')
        self.df.to_csv(path, index=False, encoding="utf-8")
        print(f"✅ Hasil disimpan ke: {path.resolve()}")
        return self


# ============================================================
# BAGIAN 2: FUNGSI PEMBANTU (UTILITY FUNCTIONS)
# ============================================================

def buat_data_contoh(path_output: str = "nilai_mahasiswa.csv"):
    """
    Membuat file CSV contoh untuk keperluan testing.
    Di dunia nyata, data ini berasal dari sistem akademik.
    """
    np.random.seed(42)  # agar hasil acak bisa direproduksi
    
    nama_list = [
        "Andi Pratama", "Budi Santoso", "Cici Rahayu", 
        "Dedi Kurniawan", "Eka Fitriani", "Fajar Nugroho",
        "Gita Permata", "Hendra Wijaya", "Indah Sari", "Joko Susilo"
    ]
    
    data = {
        "nama": nama_list,
        "npm": [f"2021{str(i+1).zfill(6)}" for i in range(len(nama_list))],
        "tugas": np.random.randint(60, 100, size=len(nama_list)),
        "uts": np.random.randint(50, 95, size=len(nama_list)),
        "uas": np.random.randint(55, 100, size=len(nama_list))
    }
    
    df = pd.DataFrame(data)
    df.to_csv(path_output, index=False)
    print(f"✅ Data contoh dibuat: {path_output}")
    return path_output


# ============================================================
# BAGIAN 3: MAIN — TITIK MASUK PROGRAM
# ============================================================

if __name__ == "__main__":
    # Blok ini hanya dijalankan saat file ini dieksekusi langsung
    # (tidak dijalankan saat file di-import oleh file lain)
    
    print("🚀 Memulai Sistem Analisis Nilai Mahasiswa\n")
    
    # Buat data contoh
    path_csv = buat_data_contoh()
    
    # Jalankan analisis menggunakan method chaining
    analis = AnalisNilai(path_csv)
    analis.hitung_nilai_akhir().tampilkan_statistik().ekspor_hasil("hasil_analisis.csv")
    
    print("\n✅ Selesai!")
