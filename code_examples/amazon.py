import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon',
    'url': 'https://www.amazon.co.uk/dp/B0BDJ279KF',
    'parse': True
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),  # Your credentials go here
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())
