# Contoh Program File Handling di Python

# 1. Membaca Isi File
try:
    with open('data.txt', 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File tidak ditemukan.")

# 2. Menulis Data ke dalam File
try:
    myText = "Saya sedang belajar Python 01."
    with open('data.txt', 'w') as file:
        file.write(myText)
        print("Data berhasil ditulis.")
except Exception as e:
    print(f"Error: {e}")

# 3. Membaca dan Menulis Data ke dalam File
try:
    myText = "Saya sedang belajar Python 02."
    with open('data.txt', 'w') as file:
        file.write(myText)
    with open('data.txt', 'r') as file:
        data = file.read()
        print(data)
except Exception as e:
    print(f"Error: {e}")

# 4. Membaca dan Menulis Data ke dalam File dengan Mode Append
try:
    myText = "Saya sedang belajar Python 03."
    with open('data.txt', 'a') as file:
        file.write(myText)
    with open('data.txt', 'r') as file:
        data = file.read()
        print(data)
except Exception as e:
    print(f"Error: {e}")

# 5. Membaca dan Menulis Data ke dalam File dengan Mode Append dan Read
try:
    myText = "Saya sedang belajar Python 04."
    with open('data.txt', 'a') as file:
        file.write(myText)
    with open('data.txt', 'r') as file:
        data = file.read()
        print(data)
except Exception as e:
    print(f"Error: {e}")

# 6. Membaca dan Menulis Data ke dalam File dengan Mode Append, Read, dan Write
try:
    myText = "Saya sedang belajar Python 05."
    with open('data.txt', 'a') as file:
        file.write(myText)
    with open('data.txt', 'r') as file:
        data = file.read()
        print(data)
except Exception as e:
    print(f"Error: {e}")

# 7. Membaca dan Menulis Data ke dalam File dengan Mode Append, Read, Write, dan Delete
try:
    myText = "Saya sedang belajar Python 06."
    with open('data.txt', 'a') as file:
        file.write(myText)
    with open('data.txt', 'r') as file:
        data = file.read()
        print(data)
except Exception as e:
    print(f"Error: {e}")