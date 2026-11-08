import requests
from pprint import pprint


# Structure payload.
payload = {
    'query': 'automotive',
    'domain': 'de',
    'start_page': 2,
    'category_id': '82400031',
    'output': ['json'],
}

# Get response.
response = requests.post(
    'https://webapi.oxylabs.io/v1/scrape/amazon/bestsellers',
    headers={'Authorization': 'Bearer YOUR_API_KEY'},  # Your API key goes here
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())
