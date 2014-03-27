import json
import requests
import time

with open('match_details.json', 'r') as json_data:
    match_details = json.load(json_data)
    for key, value in match_details.items():
        with open(key + '_match_details.json', 'w') as outfile:
            json.dump(value, outfile, indent=4, sort_keys=True)