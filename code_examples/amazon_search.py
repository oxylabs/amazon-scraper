import requests
from pprint import pprint


# Structure payload.
payload = {
    'query': 'adidas',
    'domain': 'nl',
    'start_page': 11,
    'pages': 10,
    'category_id': '16391843031',
    'merchant_id': '3AA17D2BRD4YMT0X',
    'output': ['json'],
}

# Get response.
response = requests.post(
    'https://webapi.oxylabs.io/v1/scrape/amazon/search',
    headers={'Authorization': 'Bearer YOUR_API_KEY'},  # Your API key goes here
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())
