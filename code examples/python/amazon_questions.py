import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_questions',
    'domain': 'nl',
    'query': 'AA12345678',
    'parse': True,
}


# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())