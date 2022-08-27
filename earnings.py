# make sure you install requests first using: pip install requests
import requests 
symbol = "TSLA"
x = requests.get(f'https://ab.tradeui.com/api/earnings.php?symbol={symbol}')

#return the status code a 200 means the request was successful
print(x.status_code) 
# return the response in json format: 
print(x.json())