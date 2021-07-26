import requests
from pprint import pprint

ls = list()
dup = list()

cmc_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'your own api key',
}

r = requests.get(cmc_url, headers=headers)

json = r.json()
data_cap = json['data']

#This will sort through all the ranks of crpyto currencies and display the first 10
all_crypto = json['data']

def get_rank(all_crypto):
    return all_crypto.get('rank')

all_crypto.sort(key=get_rank)
all_crypto = all_crypto[:10]

for x in all_crypto:
    dup.append(x['name'].lower())

#error_coins = ['binance-coin','usd-coin','binance-usd','xrp']

def coin_replace(coin):
  if coin == 'usd-coin':
    pass
  elif coin == 'binance-coin':
    pass
  elif coin == 'binanace-coin':
    pass
  elif coin == 'xrp':
    pass
  else:
    url = (
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=dogecoin"
    )
    url = url.replace('dogecoin', coin)
    send_server = requests.get(url)
    r2_json = send_server.json()
    r3_json = r2_json[0]
    price = r3_json['current_price']
    for x in all_crypto:
      if coin == x['name'].lower():
        ls.append((x['name'],price,'rank',x['rank']))

dup.pop(3)
dup.insert(3,'binance-coin')
dup.pop(6)
dup.insert(6,'usd-coin')
dup.pop(9)
dup.insert(9,'binance-usd')


for x in dup:
  coin_replace(x)

ls.insert(3,'Binance Coin Info not availble')
ls.insert(4,'XRP Info not availble')
ls.insert(5,'USD Coin Info not availble')
ls.insert(9,'Binance USD Info not availble')

#Final list with all crpyto s and name and price and rank!
pprint(ls)


#upload to git hub with creative title

#finish learning python