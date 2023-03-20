import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_search',
    'domain': 'nl',
    'query': 'adidas',
    'start_page': 11,
    'pages': 10,
    'parse': True,
    'context': [
        {'key': 'category_id', 'value': 16391843031},
        {'key': 'merchant_id', 'value': '3AA17D2BRD4YMT0X'}
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
