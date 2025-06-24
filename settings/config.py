import os
import json

# Apify provides the input as a JSON file at '/apify/input.json'
with open('/apify/input.json', 'r') as f:
    actor_input = json.load(f)
    
# Upwork credentials
UPWORK_USER_NAME = actor_input.get('UPWORK_USER_NAME')
UPWORK_USERNAME = actor_input.get('UPWORK_USERNAME')
UPWORK_PASSWORD = actor_input.get('UPWORK_PASSWORD')


# Chrome driver settings
CHROME_VERSIONS = [
    90,
    123,
]
MAX_ATTEMPTS = 3
