import requests

def get_live_price(coin_id):
    """
    Fetches the current price of a coin from CoinGecko.
    coin_id examples: 'bitcoin', 'ethereum', 'solana'
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        if coin_id in data:
            return data[coin_id]['usd']
        return 0
    except Exception as e:
        print(f"Error fetching price: {e}")
        return 0