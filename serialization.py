import json


## json.dumps()

JSON_DICT = {"name": "Bob", "age": 35, "city": "Seattle"}

def json_dumps(json_string):
    JSON_DATA = json.dumps(json_string)

    print(f'Type: {type(JSON_DATA)}')
    print(JSON_DATA)

## json.dump()

def json_dump(data):
    with open("json/DUMP_OUTPUT.json", "w") as f:
        json.dump(data, f)

json_dumps(JSON_DICT)
json_dump(JSON_DICT)




