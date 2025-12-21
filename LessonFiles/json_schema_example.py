from jsonschema import validate, ValidationError
from clients.authentication.authentication_schema import TokenSchema

print(TokenSchema.model_json_schema())

schema_2 = {
    'description': 'Structure description',
    'properties': {
        'tokenType': {'title': 'Tokentype', 'type': 'string'},
        'accessToken': {'title': 'Accesstoken', 'type': 'string'},
        'refreshToken': {'title': 'Refreshtoken', 'type': 'string'}
    },
    'required': ['tokenType', 'accessToken', 'refreshToken'],
    'title': 'TokenSchema',
    'type': 'object'
}


schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number" }
  },
  "required": ["name"]
}

data = {
    "name": "Alice",
    "age": 30
}

try:
    validate(instance=data, schema=schema)
    print("Данные соответствуют схеме.")
except ValidationError as e:
    print(f"Ошибка валидации: {e.message}")