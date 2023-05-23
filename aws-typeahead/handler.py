import json

# Create sample cryptocurrency data
data = [
    {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 45000.00,
        "market_cap": 842000000000,
        "volume": 18300000000
    },
    {
        "name": "Ethereum",
        "symbol": "ETH",
        "price": 3500.00,
        "market_cap": 400000000000,
        "volume": 10000000000
    },
    {
        "name": "Ripple",
        "symbol": "XRP",
        "price": 1.00,
        "market_cap": 50000000000,
        "volume": 2000000000
    },
    {
        "name": "Litecoin",
        "symbol": "LTC",
        "price": 180.00,
        "market_cap": 10000000000,
        "volume": 500000000
    }
]

# Save data to a JSON file
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

# Search data in JSON file
def search_data(filename, key, value):
    with open(filename) as file:
        data = json.load(file)
    results = [item for item in data if item.get(key) == value]
    return results

# Save data to a JSON file
save_data('cryptos.json', data)

def lambda_handler(event, context):
    # Search data in JSON file
    search_key = 'symbol'
    search_value = 'ETH'
    results = search_data('cryptos.json', search_key, search_value)

    # Print search results
    print(f"Search results for {search_key} = {search_value}:")
    for result in results:
        print(result)
