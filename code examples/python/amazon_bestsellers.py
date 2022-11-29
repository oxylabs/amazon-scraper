import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_bestsellers',
    'domain': 'com',
    'query': 'Clothing, Shoes & Jewelry',
    'start_page': 2,
    'parse': True,
    'context': [
        {'key': 'category_id', 'value': 6127770011},
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