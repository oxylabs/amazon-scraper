import fetch from 'node-fetch';

const username = 'YOUR_USERNAME';
const password = 'YOUR_PASSWORD';
const body = {
  'source': 'amazon_search',
  'domain': 'nl',
  'query': 'adidas',
  'start_page': 11,
  'pages': 10,
  'parse': true,
  'context': [
        {'key': 'category_id', 'value': 16391843031},
        {'key': 'merchant_id', 'value':'3AA17D2BRD4YMT0X'}
    ],
};
const response = await fetch('https://realtime.oxylabs.io/v1/queries', {
  method: 'post',
  body: JSON.stringify(body),
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + Buffer.from(`${username}:${password}`).toString('base64'),
  }
});

console.log(await response.json());