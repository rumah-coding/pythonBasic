import random
namas = ['adi', 'budi', 'caca', 'dedi', 'erik']
data = {nama: random.randint(1, 100) for nama in namas}
print(data)
tertinggi = max(data, key=data.get)
rerata = sum(data.values()) / len(data)
print(f"Data: {data}")
print(f"Nilai tertinggi: {tertinggi} nama dengan nilai tertinggi: {[nama for nama, nilai in data.items() if nilai == tertinggi]}")  
print(f"Rerata nilai: {rerata:.2f}")

namaTertinggi = max(data, key=data.get)
print(f"Nama dengan nilai tertinggi: {namaTertinggi} dengan nilai {data[namaTertinggi]}")   
print(data[tertinggi])
