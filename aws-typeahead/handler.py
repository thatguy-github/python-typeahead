import json
import logging
import sys
import requests


# Set up logging configuration
logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logging.info("Lambda function invoked.")


    url = "https://www.cryptocompare.com/api/data/coinlist"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Access the response data (assuming it's in JSON format)
        data = response.json()

        logging.info("Data loaded")

        # Example: Print the first coin's information
        # first_coin = next(iter(data["Data"].values()))
        # print(f"Coin Name: {first_coin['CoinName']}")
        # print(f"Symbol: {first_coin['Symbol']}")
    else:
        # Construct the response dictionary
        lambda_response = {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {"message": "bruh"}
        }
        # Return the response dictionary
        return lambda_response


    # Parse the JSON payload
    if isinstance(event, str):
        event = json.loads(event)  # Parse the event string into a dictionary

    body = event.get("body", {})
    body = event.get("queryStringParameters", {})

    # Define the ticker symbol for item we want to get or default to bitcoin
    search_value = json.loads(payload).get("name", "Bitcoin")
    logging.debug(f"Search value: {search_value}")

    # Search data in JSON file
    search_key = 'name'
    logging.debug(f"Search key: {search_key}")

    # Perform partial search on coin name
    found_coins = []
    for coin_data in data["Data"].values():
        if coin_data["CoinName"].lower().startswith(search_value.lower()):
            found_coins.append(coin_data)

    # Print the found coins
    # do a little trolling

    # Create a list to store the coin information
    coin_list = []

    # Build the coin list
    for coin in found_coins:
        coin_info = {
            "Coin Name": coin["CoinName"],
            "Symbol": coin["Symbol"]
        }
        coin_list.append(coin_info)



    # Construct the response dictionary
    lambda_response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(coin_list, indent=4)
    }

    # Return the response dictionary
    return lambda_response

logging.info("Lambda function execution completed.")

