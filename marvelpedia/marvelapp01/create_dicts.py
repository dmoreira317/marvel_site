import json


def create_character_dictionary(jsontext):
    # loading the json text into a pydict
    character_dict = json.load(jsontext)
    return character_dict
