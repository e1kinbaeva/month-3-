import schedule, time,requests

def hello_world():
    print(f"Hello world {time.ctime()}")

def backend_16_1b():
    print(f"Здравствуйте, сегодня у вас урок в 19:00")

# schedule.every().monday.at("19:58").do(backend_16_1b)

# schedule.every (2).sec.do(hello_world)
schedule.every(1).minutes.do(hello_world)
# schedule.every().day.at ('19:49').do(hello_world)
# schedule.every().monday.at("19:50").do(hello_world)
# schedule.every().day.at("19:53", "Asia/Bishkek").do(hello_world)


def get_btc_price():
    response = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    data = response.json()
    price = data['price']
    print(f"Цена биткоина на {time.ctime()}:{price} $")

# schedule.every(1).seconds.do(get_btc_price)

def get_eth_price():
    response = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=ETHUSDT")
    data = response.json()
    price = data['price']
    print(f"Цена ETH на {time.ctime()}:{price} $")

# schedule.every(1).second.do(get_eth_price)




while True:
    schedule.run_pending()
    time.sleep(1)

