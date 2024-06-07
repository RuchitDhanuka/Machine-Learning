import requests

# URL to fetch the stock data
url = 'https://www.nseindia.com/api/quote-equity?symbol=RELIANCE'

# Headers to simulate a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Make the request
response = requests.get(url, headers=headers)
data = response.json()

# Print the stock data
print(data)
