import requests
from pprint import pprint


# Structure payload.
payload = {
    'query': 'ABNP0A7Y0QWBN',
    'domain': 'de',
    'output': ['json'],
}

# Get response.
response = requests.post(
    'https://webapi.oxylabs.io/v1/scrape/amazon/sellers',
    headers={'Authorization': 'Bearer YOUR_API_KEY'},  # Your API key goes here
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())
