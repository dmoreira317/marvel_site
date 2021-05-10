import json
import sys
import html
import requests
import os
import time
import hashlib
from dotenv import load_dotenv


#This isn't linked to anything as of now

load_dotenv()
TIME_STAMP = time.time()
API_PUBLIC = os.getenv('API_PUBLIC')
API_PRIVATE = os.getenv('API_PRIVATE')
md5_origin = str(TIME_STAMP)+API_PRIVATE+API_PUBLIC
HASH_CODE = hashlib.md5(md5_origin.encode())
HASH = HASH_CODE.hexdigest()

params = {
    "apikey": API_PUBLIC,
    "ts": TIME_STAMP,
    "hash": HASH,
}
test_request = requests.get("http://gateway.marvel.com/v1/public/comics", params=params)
print(test_request)