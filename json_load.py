import json

with open("MOCK_DATA.json", "r") as fp: ## Reads the MOCK_DATA.json file
    json_data = json.load(fp) ## Stores json data to json_data variable

print(json_data) ## Prints json_data
print(type(json_data)) ## Prints data type of json_data. Output: <class 'list'>



counter = 1
for item in json_data: ## Loops each item in json_data
    print(f'{counter}.')
    json_dict = dict(item) ## Converts item to dictionary

    for key, value in json_dict.items(): ## Loops each key and value in json_dict
        print(f'{key} : {value}') ## Prints each key and value

    counter+=1    

    print('')    