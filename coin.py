# Import libraries 
import json 
import requests 
import datetime
  
# defining key/request url 
btc = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
wld = "https://api.binance.com/api/v3/ticker/price?symbol=WLDUSDT"
ada = "https://api.binance.com/api/v3/ticker/price?symbol=ADAUSDT"
floki = "https://api.binance.com/api/v3/ticker/price?symbol=FLOKIUSDT"
mana = "https://api.binance.com/api/v3/ticker/price?symbol=MANAUSDT"
bonk = "https://api.binance.com/api/v3/ticker/price?symbol=BONKUSDT"
agix = "https://api.binance.com/api/v3/ticker/price?symbol=AGIXUSDT"
xec = "https://api.binance.com/api/v3/ticker/price?symbol=XECUSDT"
volumn24h = 'https://api.binance.com/api/v3/ticker/24hr'

def getInfo():
    pass

def getPrice(symbol,ago):
    dt5min = datetime.datetime.now() - datetime.timedelta(minutes=5);
    dt4min = datetime.datetime.now() - datetime.timedelta(minutes=4);
    startTime = datetime.datetime.now()
    startTime.replace(hour=0, minute=0, second=0, microsecond=0)

    url = 'https://api.binance.com/api/v3/klines?symbol=' + symbol + 'USDT&interval=1m' \
           + '&startTime=' + str(int(startTime.timestamp())) + '000' \
           + '&endTime=' + str(int((startTime + datetime.timedelta(minutes=1)).timestamp()))+ '000'
    data = requests.get(url).json()
    return {'open': data[0][2], 'volumn': data[0][5]}

def getTime():
    pass

data = requests.get(volumn24h).json()
sum = 0
performance = 0
for item in data:
    sum+=float(item["volume"])
    performance+=float(item["priceChangePercent"])


print(f"all 24h volumn: {sum/1000000000000}K Millliards %")
print(f"24h performance avg: {performance/len(data)*100}%")

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
dt5mins = datetime.datetime.now() - datetime.timedelta(minutes=5)
print(f"{data['symbol']} 5min {dt5mins.strftime('%d-%m-%Y %H:%M:%S')} at {getPrice('ADA', 5).get('open')}")
print(f"{data['symbol']} stop limit at {data['price']} pl={exitPl}")



# AGIX
buyPrice = 1.2603
amount = 56
data = requests.get(agix).json()
pl = (float(data['price'])-buyPrice)*amount
sellPrice = 1.22
exitPl = (sellPrice-buyPrice)*amount
print(f"{data['symbol']} current price is {data['price']} invested {buyPrice*amount}USDT pl={pl}")
print(f"{data['symbol']} stop limit at {data['price']} pl={exitPl}")

# XEC
buyPrice = 0.000075*1.08
amount = 1333738.5
data = requests.get(xec).json()
pl = (float(data['price'])-buyPrice)*amount
sellPrice = 0.0000639843
exitPl = (sellPrice-buyPrice)*amount
print(f"{data['symbol']} current price is {data['price']} invested {buyPrice*amount}USDT pl={pl}")
print(f"{data['symbol']} stop limit at {data['price']} pl={exitPl}")

# BNX
buyPrice = 0.000075*1.08
amount = 1333738.5
data = requests.get(xec).json()
pl = (float(data['price'])-buyPrice)*amount
sellPrice = 0.0000639843
exitPl = (sellPrice-buyPrice)*amount
print(f"{data['symbol']} current price is {data['price']} invested {buyPrice*amount}USDT pl={pl}")
print(f"{data['symbol']} stop limit at {data['price']} pl={exitPl}")



