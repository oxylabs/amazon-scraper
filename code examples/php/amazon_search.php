<?php

$params = array(
    'source' => 'amazon_search',
    'domain' => 'nl',
    'query' => 'adidas',
    'start_page' => 11,
    'pages' => 10,
    'parse' => true,
    'context' => [
      [
        'key' => 'category_id', 
        'value' => 16391843031,
      ],
      [
        'key' => 'merchant_id',
        'value' => '3AA17D2BRD4YMT0X'
      ]
    ],
);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "https://realtime.oxylabs.io/v1/queries");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($params));
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_USERPWD, "user" . ":" . "pass1");


$headers = array();
$headers[] = "Content-Type: application/json";
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$result = curl_exec($ch);
echo $result;

if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);
}
curl_close ($ch);
?>