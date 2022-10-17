import requests
import sys


try:
    coins_to_buy = float(sys.argv[1])
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    usd_rate = r.json()["bpi"]["USD"]["rate_float"]
    print(f"${usd_rate * coins_to_buy:,}")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Request timed out")