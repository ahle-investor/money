# Import libraries 
import json 
import requests 
  
# defining key/request url 
btc = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
wld = "https://api.binance.com/api/v3/ticker/price?symbol=WLDUSDT"
ada = "https://api.binance.com/api/v3/ticker/price?symbol=ADAUSDT"
floki = "https://api.binance.com/api/v3/ticker/price?symbol=FLOKIUSDT"
mana = "https://api.binance.com/api/v3/ticker/price?symbol=MANAUSDT"
bonk = "https://api.binance.com/api/v3/ticker/price?symbol=BONKUSDT"


def getInfo():
    pass

# requesting data from url 
data = requests.get(ada).json()
print(f"{data['symbol']} price is {data['price']}")

data = requests.get(wld).json()
print(f"{data['symbol']} price is {data['price']}")

# Floki
buyPrice = 0.000249567
amount = 400693.86
data = requests.get(floki).json()
pl = (float(data['price'])-buyPrice)*amount
print(f"{data['symbol']} price is f{data['price']} pl=f{pl}")
print(pl)

# Bonk
buyPrice = 0.0000326677
amount = 4000000
data = requests.get(bonk).json()
pl = (float(data['price'])-buyPrice)*amount
sellPrice = 0.000035
exitPl = (sellPrice-buyPrice)*amount
print(f"{data['symbol']} current price is {data['price']} invested {buyPrice*amount} pl=f{pl}")
print(f"{data['symbol']} stop limit at {data['price']} pl={exitPl}")


# ADA
buyPrice = 0.0000326677
amount = 4000000
data = requests.get(ada).json()
pl = (float(data['price'])-buyPrice)*amount
sellPrice = 0.000035
exitPl = (sellPrice-buyPrice)*amount
print(f"{data['symbol']} current price is {data['price']} invested {buyPrice*amount} pl=f{pl}")
print(f"{data['symbol']} stop limit at {data['price']} pl={exitPl}")

