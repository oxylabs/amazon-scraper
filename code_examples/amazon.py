import requests
from pprint import pprint


# Structure payload.
payload = {
    'url': 'https://www.amazon.co.uk/dp/B0BDJ279KF',
    'output': ['json'],
}

# Get response.
response = requests.post(
    'https://webapi.oxylabs.io/v1/scrape/amazon',
    headers={'Authorization': 'Bearer YOUR_API_KEY'},  # Your API key goes here
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())
