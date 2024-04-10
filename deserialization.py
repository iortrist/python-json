import json

# json.load()

def read_from_json_file():
    with open("JSON_DATA.json", "r") as fp:
        JSON_DATA = json.load(fp)

    print(f'Type: {type(JSON_DATA)}')
    print(JSON_DATA)


# with open("jsonString.txt", "rb") as fp:
#     json_loads = json.loads(fp.read())

# with open("json.doc", "rb") as fp:
#     json_doc = json.loads(fp.read())


# print("json.loads(): ", type(json_loads))
# print("json.load(): ", type(json_load))

# print(json_doc)

read_from_json_file()