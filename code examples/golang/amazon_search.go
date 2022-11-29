package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	const Username = "YOUR_USERNAME"
	const Password = "YOUR_PASSWORD"

	payload := map[string]interface{}{
		"source":     "amazon_search",
		"domain":     "nl",
		"query":      "adidas",
		"start_page": 11,
		"pages":      10,
		"parse":      true,
		"context": []map[string]interface{}{
			{"key": "category_id", "value": 16391843031},
			{"key": "merchant_id", "value": "3AA17D2BRD4YMT0X"},
		},
	}

	jsonValue, _ := json.Marshal(payload)

	client := &http.Client{}
	request, _ := http.NewRequest("POST",
		"https://realtime.oxylabs.io/v1/queries",
		bytes.NewBuffer(jsonValue),
	)

	request.SetBasicAuth(Username, Password)
	response, _ := client.Do(request)

	responseText, _ := ioutil.ReadAll(response.Body)
	fmt.Println(string(responseText))
}
