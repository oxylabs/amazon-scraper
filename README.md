# Amazon Scraper

### Overview

Below is a quick overview of all the available data `source` values we support with Amazon.

| Source               | Description                                                  | Structured data     |
| -------------------- | ------------------------------------------------------------ | ------------------- |
| `amazon`             | Submit any Amazon URL you like.                              | Depends on the URL. |
| `amazon_bestsellers` | List of best seller items in a taxonomy node of your choice. | Yes                 |
| `amazon_pricing`     | List of offers available for an ASIN of your choice.         | Yes.                |
| `amazon_product`     | Product page of an ASIN of your choice.                      | Yes.                |
| `amazon_questions`   | Q\&A page of an ASIN of your choice.                         | Yes.                |
| `amazon_reviews`     | Reviews page of an ASIN of your choice.                      | Yes.                |
| `amazon_search`      | Search results for a search term of your choice.             | Yes.                |
| `amazon_sellers`     | Seller information of a seller of your choice.               | Yes.                |

### URL

The `amazon` source is designed to retrieve the content from various Amazon URLs. Instead of sending multiple parameters, you can provide us with a direct URL to the required Amazon page. We do not strip any parameters or alter your URLs in any way.

#### **Query parameters**

| Parameter                                                   | Description                                                                                                                                       | Default Value |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
|  <mark style="background-color:green;">**`source`**</mark>  | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#source).                                              | N/A           |
|  <mark style="background-color:green;">**`url`**</mark>     | Direct URL (link) to Amazon page                                                                                                                  | -             |
| `user_agent_type`                                           | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#user_agent_type). | `desktop`     |
| `render`                                                    | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#render)                         | -             |
| `callback_url`                                              | URL to your callback endpoint. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#callback_url).                     | -             |
| `parse`                                                     | `true` will return structured data, as long as the URL submitted is for one of the page types we can parse.                                       | `false`       |

&#x20;   <mark style="background-color:green;"></mark> - required parameter

#### Python code example

In the code example below, we make a request to retrieve the Amazon product page for `ASIN AA12345678` .

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon',
    'url': 'https://www.amazon.co.uk/dp/AA12345678',
    'parse': True
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('YOUR_USERNAME', 'YOUR_PASSWORD'), #Your credentials go here
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())
```

To see the response example with retrieved data, download [**this** **sample output**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiwDdoZGfMbUe5cRL2417%2Fuploads%2FTsZ8TZKgQe4y7BT6DgKg%2Famazon.json?alt=media\&token=be9d00d0-d3e3-443b-be67-26cbdbcabc5d) in JSON format.

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/amazon-scraper/tree/main/code%20examples)

### Search

The `amazon_search` source is designed to retrieve Amazon search result pages.

#### Query parameters

| Parameter                                                   | Description                                                                                                                                       | Default Value   |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
|  <mark style="background-color:green;">**`source`**</mark>  | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#source).                                              | `amazon_search` |
| `domain`                                                    | Domain localization for Amazon. The full list of available domains can be found [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#domain).                           | `com`           |
|  <mark style="background-color:green;">**`query`**</mark>   | UTF-encoded keyword                                                                                                                               | -               |
| `start_page`                                                | Starting page number                                                                                                                              | `1`             |
| `pages`                                                     | Number of pages to retrieve                                                                                                                       | `1`             |
| `geo_location`                                              | The _Deliver to_ location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#geo_location)**.**                               | -               |
| `user_agent_type`                                           | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#user_agent_type). | `desktop`       |
| `render`                                                    | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#render)                         | -               |
| `callback_url`                                              | URL to your callback endpoint. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#callback_url).                     | -               |
| `parse`                                                     | `true` will return structured data.                                           | -               |
| <p><code>context</code>:<br><code>category_id</code></p>    | Search for items in a particular browse node (product category).                                                                                  | -               |
| <p><code>context</code>:<br><code>merchant_id</code></p>    | Search for items sold by a particular seller.                                                                                                     | -               |

&#x20;   <mark style="background-color:green;"></mark> - required parameter

#### Python code example

In the code example below, we make a request to retrieve product page for ASIN `AA12345678`on `amazon.nl` marketplace. In case the ASIN provided is a parent ASIN, we ask Amazon to return a product page of an automatically-selected variation.

```python
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
        {'key': 'merchant_id', 'value':'3AA17D2BRD4YMT0X'}
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
```

 To see the response example with retrieved data, download [**this** **sample output**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiwDdoZGfMbUe5cRL2417%2Fuploads%2Fyg8tdLTqrajAxhtjiuR5%2Famazon\_search.json?alt=media\&token=f02b1ceb-70f6-45cd-9f7c-7247196b2bd6) file in JSON format.
 
Code examples for other languages can be found [**here.**](https://github.com/oxylabs/amazon-scraper/tree/main/code%20examples)
 
### Product

The `amazon_product` data source is designed to retrieve Amazon product pages.

#### Query parameters

| Parameter                                                       | Description                                                                                                                                                                                                                                                                | Default Value    |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
|  <mark style="background-color:green;">**`source`**</mark>      | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#source).                                                                                                                                                                       | `amazon_product` |
| `domain`                                                        | Domain localization for Amazon. The full list of available domains can be found [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#domain).                                                                                                                                                    | `com`            |
|  <mark style="background-color:green;">**`query`**</mark>       | 10-symbol ASIN code                                                                                                                                                                                                                                                        | -                |
| `geo_location`                                                  | The _Deliver to_ location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#geo_location)**.**                                                                                                                                                        | -                |
| `user_agent_type`                                               | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#user_agent_type).                                                                                                                          | `desktop`        |
| `render`                                                        | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#render)                                                                                                                                                 |                  |
| `callback_url`                                                  | URL to your callback endpoint. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#callback_url).                                                                                                                                              | -                |
| `parse`                                                         | `true` will return structured data.                                                                                                                                                           | -                |
| <p><code>context</code>:<br><code>autoselect_variant</code></p> | To get accurate pricing/buybox data, set this parameter to `true` (which tells us to append the `th=1&psc=1` URL parameters to the end of the product URL). To get an accurate representation of the parent ASIN's product page, omit this parameter or set it to `false`. | `false`          |

&#x20; <mark style="background-color:green;"></mark> - required parameter

#### Python code example

In the code example below, we make a request to retrieve product page for ASIN `AA12345678`on `amazon.nl` marketplace. In case the ASIN provided is a parent ASIN, we ask Amazon to return a product page of an automatically-selected variation.

```python
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
```

To see the response example with retrieved data, download [**this** **sample output**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiwDdoZGfMbUe5cRL2417%2Fuploads%2Fjj4ahNp1FpIqjY2JcSqz%2Famazon\_product.json?alt=media\&token=42016a49-9790-4671-9022-bb0feed79d1a) file in JSON format.

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/amazon-scraper/tree/main/code%20examples)
 
### Offer listing

The `amazon_pricing` data source is designed to retrieve Amazon product offer listings.

#### Query parameters

| Parameter                                                   | Description                                                                                                                                       | Default Value    |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
|  <mark style="background-color:green;">**`source`**</mark>  | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#source).                                              | `amazon_pricing` |
| `domain`                                                    | Domain localization for Amazon. The full list of available domains can be found [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#domain).                           | `com`            |
|  <mark style="background-color:green;">**`query`**</mark>   | 10-symbol ASIN code                                                                                                                               | -                |
| `start_page`                                                | Starting page number                                                                                                                              | `1`              |
| `pages`                                                     | Number of pages to retrieve                                                                                                                       | `1`              |
| `geo_location`                                              | The _Deliver to_ location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#geo_location).                                   | -                |
| `user_agent_type`                                           | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#user_agent_type). | `desktop`        |
| `render`                                                    | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#render)                         |                  |
| `callback_url`                                              | URL to your callback endpoint. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#callback_url).                     | -                |
| `parse`                                                     | `true` will return structured data.                             | -                |

&#x20;   <mark style="background-color:green;"></mark> - required parameter

#### Python code example

In the code examples below, we make a request to retrieve product offer listing page for ASIN `AA12345678` on `amazon.nl`&#x20; marketplace.

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_pricing',
    'domain': 'nl',
    'query': 'AA12345678',
    'parse': True,
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
```

To see what the parsed output looks like, download [**this**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiwDdoZGfMbUe5cRL2417%2Fuploads%2FhGVtkmLp7gccwTLCJzLY%2Famazon\_pricing.json?alt=media\&token=a30a8253-225f-44c2-880b-850e94e23c21) JSON file.

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/amazon-scraper/tree/main/code%20examples)
 
### Reviews

The `amazon_reviews` data source is designed to retrieve Amazon product review pages of an ASIN of your choice.

#### Query parameters

| Parameter                                                   | Description                                                                                                                                       | Default Value    |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
|  <mark style="background-color:green;">**`source`**</mark>  | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#source).                                              | `amazon_reviews` |
| `domain`                                                    | Domain localization for Amazon. The full list of available domains can be found [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#domain).                           | `com`            |
|  <mark style="background-color:green;">**`query`**</mark>   | 10-symbol ASIN code                                                                                                                               | -                |
| `geo_location`                                              | The _Deliver to_ location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#geo_location).                                   | -                |
| `user_agent_type`                                           | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#user_agent_type). | `desktop`        |
| `start_page`                                                | Starting page number                                                                                                                              | `1`              |
| `pages`                                                     | Number of pages to retrieve                                                                                                                       | `1`              |
| `render`                                                    | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#render)                         |                  |
| `callback_url`                                              | URL to your callback endpoint. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#callback_url).                     | -                |
| `parse`                                                     | `true` will return structured data.                                  | -                |

&#x20;   <mark style="background-color:green;"></mark> - required parameter

#### Python code example

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_reviews',
    'domain': 'nl',
    'query': 'AA12345678',
    'parse': True,
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
```

To see the response example with retrieved data, download this [**sample** **output**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiwDdoZGfMbUe5cRL2417%2Fuploads%2F4Fx7BNOyFLw4rU6dJGDH%2Famazon\_reviews.json?alt=media\&token=f1845f29-2286-41a3-9ac5-834a89b345c5) file in JSON format.

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/amazon-scraper/tree/main/code%20examples)

### Questions & Answers

The `amazon_questions` data source is designed to retrieve any particular product's Questions & Answers pages.

#### Query parameters

| Parameter                                                   | Description                                                                                                                                       | Default Value      |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
|  <mark style="background-color:green;">**`source`**</mark>  | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#source).                                              | `amazon_questions` |
| `domain`                                                    | Domain localization for Amazon. The full list of available domains can be found [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#domain).                           | `com`              |
|  <mark style="background-color:green;">**`query`**</mark>   | 10-symbol ASIN code                                                                                                                               | -                  |
| `geo_location`                                              | The _Deliver to_ location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#geo_location).                                   | -                  |
| `user_agent_type`                                           | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#user_agent_type). | `desktop`          |
| `render`                                                    | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#render)****                         |                    |
| `callback_url`                                              | URL to your callback endpoint. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#callback_url).                     | -                  |
| `parse`                                                     | `true` will return structured data.                   | -                  |

&#x20;   <mark style="background-color:green;"></mark> - required parameter

#### Python code example

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_questions',
    'domain': 'nl',
    'query': 'AA12345678',
    'parse': True,
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
```

To see the response example with retrieved data, download this [**sample** **output**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiwDdoZGfMbUe5cRL2417%2Fuploads%2F1i8qUTsaifrfTht9VdXK%2Famazon\_questions.json?alt=media\&token=a59d9850-d79b-40bc-a2a6-bdd802eafd6b) file in JSON format.

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/amazon-scraper/tree/main/code%20examples)

### Best Sellers

The `amazon_bestsellers` data source is designed to retrieve Amazon Best Sellers pages.

#### Query parameters

| Parameter                                                   | Description                                                                                                                                       | Default Value        |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
|  <mark style="background-color:green;">**`source`**</mark>  | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#source).                                              | `amazon_bestsellers` |
| `domain`                                                    | Domain localization for Amazon. The full list of available domains can be found [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#domain).                           | `com`                |
| `query`                                                     | Department name. Example: `Clothing, Shoes & Jewelry`                                                                                             | -                    |
| `start_page`                                                | Starting page number                                                                                                                              | `1`                  |
| `pages`                                                     | Number of pages to retrieve                                                                                                                       | `1`                  |
| `geo_location`                                              | The _Deliver to_ location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#geo_location).                                   | -                    |
| `user_agent_type`                                           | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#user_agent_type). | `desktop`            |
| `render`                                                    | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#render)                        |                      |
| `callback_url`                                              | URL to your callback endpoint. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#callback_url).                     | -                    |
| `parse`                                                     | `true` will return structured data.                                                                                                               | -                    |
| <p><code>context</code>:<br><code>category_id</code></p>    | Search for items in a particular browse node (product category).                                                                                  | -                    |

&#x20;   <mark style="background-color:green;"></mark> - required parameter

#### Python code example

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_bestsellers',
    'domain': 'com',
    'query': 'Clothing, Shoes & Jewelry',
    'start_page': 2,
    'parse': True,
    'context': [
        {'key': 'category_id', 'value': 6127770011},
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
```

To see the response example with retrieved data, download this [**sample output**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiwDdoZGfMbUe5cRL2417%2Fuploads%2Frf2S2YKKlEEhu4cCoW6b%2Famazon\_bestsellers.json?alt=media\&token=6b4b3817-5a6e-4095-96b0-81d8d9d0883f) file in JSON format.

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/amazon-scraper/tree/main/code%20examples)

### Sellers

The `amazon_sellers` data source is designed to retrieve Amazon Sellers pages.&#x20;

#### Query parameters

| Parameter                                                   | Description                                                                                                                                                                                                                                                                      | Default Value    |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
|  <mark style="background-color:green;">**`source`**</mark>  | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#source).                                                                                                                                                                             | `amazon_sellers` |
| `domain`                                                    | Domain localization for Amazon. The full list of available domains can be found [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#domain).                                                                                                                                                          | `com`            |
|  <mark style="background-color:green;">**`query`**</mark>   | 13-character seller ID                                                                                                                                                                                                                                                           | -                |
| `geo_location`                                              | The _Deliver to_ location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon/parameter-values#geo_location).                                                                                                                                                                  | -                |
| `user_agent_type`                                           | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#user_agent_type).                                                                                                                                | `desktop`        |
| `render`                                                    | Enables JavaScript rendering. [**More info.**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#render)                                                                                                                                                        |                  |
| `callback_url`                                              | URL to your callback endpoint. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#callback_url).                                                                                                                                                    | -                |
| `parse`                                                     | `true` will return structured data. Please note that right now we only support parsed output for `desktop` device type. However, there is no apparent reason to get sellers pages with any other device type, as seller data is going to be exactly the same across all devices. | -                |

&#x20;   <mark style="background-color:green;"></mark> - required parameter

#### Python code example

In the code examples below, we make a request to retrieve the seller page for seller ID `ABNP0A7Y0QWBN` on `amazon.de` marketplace.

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_sellers',
    'domain': 'de',
    'query': 'ABNP0A7Y0QWBN',
    'parse': True
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
```

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/amazon-scraper/tree/main/code%20examples)

Oxylabs' Amazon Scraper API is an ideal option for scraping publicly-available data from any page of Amazon, be that reviews, pricing, or product information. If you want to discuss upgrading to any of our plans or have questions related to Amazon Scraper API, don't hesitate to [**get in touch with our sales team!**](mailto:hello@oxylabs.io) 
