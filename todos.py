import json
import requests



response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

print(type(todos))

for item in todos:

    items = dict(item)

    for key, value in items.items():
        
        print(f'{key} : {value}')
    
    print("")