# Contoh program inheritance di Python untuk menunjukkan konsep inheritance kepada pemula

# Definisi class Mammal (ibu kelas)
class Mammal:
    def __init__(self, name):
        self.name = name

    # Method untuk bergerak
    def move(self):
        print(f"{self.name} sedang berjalan")

    # Method untuk melahirkan
    def give_birth(self):
        print(f"{self.name} telah melahirkan")


# Definisi class Dog (turunan dari Mammal)
class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)  # Panggil konstruktor ibu kelas
        self.breed = breed

    # Method untuk menggonggong
    def bark(self):
        print(f"{self.name} sedang menggonggong")


# Definisi class Cat (turunan dari Mammal)
class Cat(Mammal):
    def __init__(self, name, color):
        super().__init__(name)  # Panggil konstruktor ibu kelas
        self.color = color

    # Method untuk melacak
    def pounce(self):
        print(f"{self.name} sedang melacak")


# Buat objek Dog dan Cat
my_dog = Dog("Fido", "Pembroke Welsh Corgi")
my_cat = Cat("Whiskers", "hitam")

# Panggil method pada objek Dog dan Cat
my_dog.move()
my_dog.give_birth()
my_dog.bark()

print("\n")

my_cat.move()
my_cat.give_birth()
my_cat.pounce()