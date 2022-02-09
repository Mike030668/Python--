import requests
import pprint

url = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(url)

print(type(response), dir(response))

#https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP
print(response.status_code)

#print(response.text)

data = response.json()
pprint.pprint(data)

params = {
 'Valute': "AUD"
}

response = requests.get(url, params = params)
#print(response.status_code)

#print(response.text)