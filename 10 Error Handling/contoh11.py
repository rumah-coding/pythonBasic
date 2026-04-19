import asyncio

async def cek_ketersediaan_async(file_name):
    try:
        with open(file_name, 'r') as file:
            await asyncio.sleep(0)
            return True
    except FileNotFoundError:
        return False

def pembaca_file():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(cek_ketersediaan_async('nama_file.txt'))
    if result:
        print("File ada")
    else:
        print("File tidak ada")
