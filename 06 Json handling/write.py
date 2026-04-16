import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "Jakarta"  
}

with open('data.json', 'w') as file:
    json.dump(data, file)