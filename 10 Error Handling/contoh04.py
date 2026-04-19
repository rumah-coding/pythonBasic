def pembilangan():
    try:
        a = int(input("Masukkan Angka Pertama: "))
        b = int(input("Masukkan Angka Kedua: "))
        return a / b
    except ZeroDivisionError as e:
        print(f"Maaf, tidak bisa membagi dengan angka 0. {str(e)}")
    finally:
        print("Selesai!")

print(pembilangan() )