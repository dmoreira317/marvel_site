import sys
import requests
import os
import time
import hashlib
from dotenv import load_dotenv
from django import template


#This isn't linked to anything as of now

# Request to Marvel's dev site
def API_request(url):
    # Loading keys
    load_dotenv()
    TIME_STAMP = time.time()
    API_PUBLIC = os.getenv('API_PUBLIC')
    API_PRIVATE = os.getenv('API_PRIVATE')
    
    #Generating requested hash as parameter
    md5_origin = str(TIME_STAMP)+API_PRIVATE+API_PUBLIC
    HASH_CODE = hashlib.md5(md5_origin.encode())
    HASH = HASH_CODE.hexdigest()

    # defining params and making the request
    params = {
        "apikey": API_PUBLIC,
        "ts": TIME_STAMP,
        "hash": HASH,
    }
    request = requests.get(url, params=params)
    return request.text

# test search
#url = "http://gateway.marvel.com/v1/public/comics"
#API_request(url)