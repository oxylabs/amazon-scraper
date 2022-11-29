curl --user USERNAME:PASSWORD \
'https://realtime.oxylabs.io/v1/queries' \
-H "Content-Type: application/json" \
-d '{"source": "amazon", "url": "https://www.amazon.co.uk/dp/AA12345678", "parse": true}'