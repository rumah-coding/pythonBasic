def tentukanPredikat(nilai:float, sistem:str="huruf"):
    """
    Tentukan predikat berdasarkan nilai ujian.

    Args:
        nilai  : nilai ujian dalam rentang 0-100
        sistem : 'huruf' untuk A/B/C/D, '4.0' untuk skala 4.0

    Returns:
        string predikat sesuai sistem yang dipilih

    Raises:
        ValueError: jika nilai di luar rentang 0-100
        ValueError: jika sistem tidak dikenal

    Example:
        >>> tentukan_predikat(85)
        'A'
        >>> tentukan_predikat(85, '4.0')
        '4.0'
    """
    if not 0<=nilai<=100:
        raise ValueError("Nilai harus antara 0 dan 100")
    if sistem=="huruf":
        if nilai>=85: return "A"
        elif nilai>=70: return "B"
        elif nilai>=60: return "C"
        else : return "D"      
    elif sistem=="4.0":
        if nilai>=85: return "4.0"
        elif nilai>=70: return "3.0"
        elif nilai>=60:return "2.0"
        else:
            return "1.0"
    else:
        raise ValueError("Sistem Tidak dikenal")

#test
for n in [95, 85, 75, 65, 55]:
    print(f"Nilai: {n} -> Predikat (huruf): {tentukanPredikat(n)}")
    print(f"Nilai: {n} -> Predikat (4.0): {tentukanPredikat(n, '4.0')}")

#List Comprehension
nilai_kelas = [95, 85, 75, 65, 55, 45, 35,90]
nilai_lulus = [n for n in nilai_kelas if n>=65]
print("Nilai Kelas:", nilai_kelas)
print("Nilai Lulus:", nilai_lulus)  
nilai_normalisasi = [ (n - min(nilai_kelas))/(max(nilai_kelas)-min(nilai_kelas)) for n in nilai_kelas]
print("Nilai Normalisasi:", nilai_normalisasi)  

#fungsi sebagai argumen
def terapkan(data:list, fungsi):
    return [fungsi(x) for x in data]

print("Predikat Huruf:", terapkan(nilai_kelas, lambda n: tentukanPredikat(n)))
print(terapkan(nilai_kelas, lambda x:tentukanPredikat(x, '4.0')))  

