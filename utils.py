import jsonschema
from jsonschema import validate

input_json_schema = {"type": "object",
                     "properties": {"date": {"type": "string", "format": "date-time"},  # TODO обновить формат
                                    "periods": {"type": "integer", "minimum": 1, "maximum": 60},
                                    "amount": {"type": "integer", "minimum": 10000, "maximum": 3000000},
                                    "rate": {"type": "number", "minimum": 1, "maximum": 8}, },
                     "minProperties": 1}


def validate_json(input_json):
    try:
        validate(instance=input_json, schema=input_json_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True
