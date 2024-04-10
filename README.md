## Module Importation
```sh
import json
```

## Python JSON
- **JSON** stands for ***JavaScript Object Notation***. 
- It is used for storing and exchanging data.
- Python has a built-in package called json, which provides functions for encoding and decoding JSON data.

## Serialization
- Serialization refers to the general process of converting any Python object (dictionaries, lists, etc.) into a JSON string representation.
- Use **json.dump()** when writing JSON representation of Python data in a file.
- User **json.dumps()** when working with JSON data as a string for further processing, transmission over a network, or temporary storage.

## Deserialization
- Deserialization boils down to reading JSON data from a file/string and converting it into usable Python object.
- Use **json.load()** when JSON data are stored in a file.
- Use **json.loads()** when working with JSON data in string format (e.g., received from an API or another program).

## Basic Workflow
1. Import the json package.
2. Read the data with load() or loads().
3. Process the data
4. Write the altered data with dump() or dumps().


