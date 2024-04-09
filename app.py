import json

## Open MOCK_DATA.json file

with open("MOCK_DATA.json", "rb") as fp:
        mock_data = json.load(fp)

        # print(mock_data)


mock_data_dict ={"First":{
  "first_name": "Diarmid",
  "last_name": "Gerrish",
  "email": "dgerrish0@tumblr.com",
  "gender": "Male"
},
"Second":{
  "first_name": "Beverlee",
  "last_name": "Hartman",
  "email": "bhartman1@mapy.cz",
  "gender": "Female"
}, 
"Third":{
  "first_name": "Aguistin",
  "last_name": "Simonaitis",
  "email": "asimonaitis2@independent.co.uk",
  "gender": "Male"
}}
json_string = json.dumps(mock_data_dict, indent=4)

with open("DUMPS_OUTPUT.json", "w") as fp:
        fp.write(json_string)



