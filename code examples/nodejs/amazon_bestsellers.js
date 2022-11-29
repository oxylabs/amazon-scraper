import fetch from 'node-fetch';

const username = 'YOUR_USERNAME';
const password = 'YOUR_PASSWORD';
const body = {
  'source': 'amazon_bestsellers',
  'domain': 'com',
  'query': 'Clothing, Shoes & Jewelry',
  'start_page': 2,
  'parse': true,
  'context': [
      {'key': 'category_id', 'value': 6127770011},
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