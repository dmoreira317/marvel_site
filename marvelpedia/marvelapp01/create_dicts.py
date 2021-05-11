import json


def create_character_dictionary(jsontext):
    # loading the json text into a pydict
    character_dict = {}
    character_dict_original = json.loads(jsontext)

    #saving only data to be shown into an array.
    character_dict["name"] = character_dict_original["data"]["results"][0]["name"]
    character_dict["description"] = character_dict_original["data"]["results"][0]["description"]
    character_dict["thumbnail"] = character_dict_original["data"]["results"][0]["thumbnail"]["path"]
    return character_dict
