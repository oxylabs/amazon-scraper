import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_product',
    'domain': 'nl',
    'query': 'AA12345678',
    'parse': True,
    'context': [
    {
      'key': 'autoselect_variant', 'value': true
    }],
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