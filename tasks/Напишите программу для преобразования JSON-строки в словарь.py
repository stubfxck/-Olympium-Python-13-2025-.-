import json

json_string = '{"name": "Алексей", "age": 20, "city": "Казань"}'

data = json.loads(json_string)

print(data["age"])