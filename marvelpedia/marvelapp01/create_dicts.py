import json


def create_character_dictionary(jsontext):
    # loading the json text into a pydict
    character_dict = json.loads(jsontext)
    return character_dict
