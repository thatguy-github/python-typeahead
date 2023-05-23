import json
import logging
import sys

# Set up logging configuration
logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


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
    logging.debug(f"Data saved to {filename}")

# Search data in JSON file
def search_data(filename, key, value):
    with open(filename) as file:
        data = json.load(file)
    results = [item for item in data if item.get(key) == value]
    return results

# Save data to a JSON file
save_data('cryptos.json', data)

logging.info("started.")

def lambda_handler(event, context):
    logging.info("Lambda function invoked.")

    # Parse the JSON payload
    if isinstance(event, str):
        event = json.loads(event)  # Parse the event string into a dictionary

    body = event.get("body", {})
    payload = json.dumps(body)  # Convert the payload dictionary to a JSON string

    # Define the ticker symbol for item we want to get or default to bitcoin
    search_value = json.loads(payload).get("name", "Bitcoin")
    logging.debug(f"Search value: {search_value}")

    # Search data in JSON file
    search_key = 'name'
    logging.debug(f"Search key: {search_key}")

    results = search_data('cryptos.json', search_key, search_value)

    # Print search results
    logging.info(f"Search results for {search_key} = {search_value}:")
    for result in results:
        logging.info(result)

    logging.info("Lambda function execution completed.")

