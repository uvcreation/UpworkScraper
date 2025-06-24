import os
import json

# Try input file first, then environment variables
UPWORK_USER_NAME = None
UPWORK_USERNAME = None
UPWORK_PASSWORD = None

# Method 1: Try Apify input file
try:
    if os.path.exists('/apify/input.json'):
        with open('/apify/input.json', 'r') as f:
            actor_input = json.load(f)
        UPWORK_USER_NAME = actor_input.get('UPWORK_USER_NAME')
        UPWORK_USERNAME = actor_input.get('UPWORK_USERNAME')
        UPWORK_PASSWORD = actor_input.get('UPWORK_PASSWORD')
except:
    pass

# Method 2: Fallback to environment variables
if not UPWORK_USER_NAME:
    UPWORK_USER_NAME = os.getenv('UPWORK_USER_NAME')
if not UPWORK_USERNAME:
    UPWORK_USERNAME = os.getenv('UPWORK_USERNAME')
if not UPWORK_PASSWORD:
    UPWORK_PASSWORD = os.getenv('UPWORK_PASSWORD')

# Validate
if not all([UPWORK_USER_NAME, UPWORK_USERNAME, UPWORK_PASSWORD]):
    raise ValueError("❌ Missing credentials! Provide via Apify input or environment variables.")

CHROME_VERSIONS = [90, 123]
MAX_ATTEMPTS = 3
