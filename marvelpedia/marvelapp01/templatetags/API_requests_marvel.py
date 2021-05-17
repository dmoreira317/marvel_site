# This copy of API request was created to access it from Django 
# labels if some request is needed to be made as filter

import sys
import requests
import os
import time
import hashlib
from dotenv import load_dotenv
from django import template

register = template.Library()

# Request to Marvel's dev site
def API_request(url):
    # Loading keys
    load_dotenv()
    TIME_STAMP = time.time()
    API_PUBLIC = os.getenv('API_PUBLIC')
    API_PRIVATE = os.getenv('API_PRIVATE')
    
    # Generating requested hash as parameter
    md5_origin = str(TIME_STAMP)+API_PRIVATE+API_PUBLIC
    HASH_CODE = hashlib.md5(md5_origin.encode())
    HASH = HASH_CODE.hexdigest()

    # Defining params and making the request
    params = {
        "apikey": API_PUBLIC,
        "ts": TIME_STAMP,
        "hash": HASH,
    }
    test_request = requests.get(url, params=params)
    return test_request.text

register.filter("API_request", API_request)
# test search
#url = "http://gateway.marvel.com/v1/public/comics"
#API_request(url)