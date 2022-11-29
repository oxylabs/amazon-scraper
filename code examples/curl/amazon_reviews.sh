curl --user user:pass1 'https://realtime.oxylabs.io/v1/queries' -H "Content-Type: application/json"
 -d '{"source": "amazon_reviews", "domain": "nl", "query": "AA12345678", "parse": true}'