# In this file i create some utilities to modify strings and create dictionaries.

import json

# This func takes the json from the url request made in character search and makes it a dict
def create_character_dictionary(jsontext):
    # loading the json text into a pydict
    character_dict = {}
    character_dict_original = json.loads(jsontext)

    #saving only data to be shown into an array.
    character_dict["name"] = character_dict_original["data"]["results"][0]["name"]
    character_dict["description"] = character_dict_original["data"]["results"][0]["description"]
    character_dict["thumbnail"] = character_dict_original["data"]["results"][0]["thumbnail"]
    
    return character_dict

# This func takes the dictionary where image info is available 
# and creates a string containing proper URL path, 
# as required by Marvel to access it
def image_view_generator(dict, size):
    extension = dict["extension"]
    image_path = dict["path"] + f"/{size}.{extension}"

    return image_path
