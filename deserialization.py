import json

## json.load() - Reads file object containing JSON data

## Reading from a json file
def read_from_json_file(): 
    with open("JSON_DATA.json", "r") as fp:
        JSON_DATA = json.load(fp)

    print(f'Type: {type(JSON_DATA)}')
    print(JSON_DATA)

## Reading from a txt file
def read_from_txt_file():
    with open("JSON_DATA.txt", "r") as fp:
        JSON_DATA = json.load(fp)

    print(f'Type: {type(JSON_DATA)}')
    print(JSON_DATA)

## Reading from a doc file
def read_from_doc_file():
    with open("JSON_DATA.doc", "r") as fp:
        JSON_DATA = json.load(fp)

    print(f'Type: {type(JSON_DATA)}')
    print(JSON_DATA)



## json.loads() - Reads string containing valid JSON data

JSON_STRING = '{"name": "Alice", "age": 30, "city": "New York"}'

def json_loads(json_string):
    JSON_DATA = json.loads(json_string)

    print(f'Type: {type(JSON_DATA)}')
    print(JSON_DATA)


# read_from_json_file()
# read_from_txt_file()
# read_from_doc_file()
json_loads(JSON_STRING)