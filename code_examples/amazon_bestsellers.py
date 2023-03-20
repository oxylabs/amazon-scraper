import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_bestsellers',
    'domain': 'de',
    'query': 'automotive',
    'start_page': 2,
    'parse': True,
    'context': [
        {'key': 'category_id', 'value': 82400031},
    ],
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
