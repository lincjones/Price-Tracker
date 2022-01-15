from bs4 import BeautifulSoup as bs
import requests
import time
from plyer import notification

minutes = input("How often should I check? (minutes): ")
currPrice = input("How much does it cost currently(with commas): ")
uurl = input("What is the product's amazon url: ")

loop = True

while loop:
    headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip', 
    'DNT' : '1', # Do Not Track Request Header 
    'Connection' : 'close'
    }
    url = uurl

    result = requests.get(url, headers=headers)

    doc = bs(result.text, "html.parser")

    prices = doc.find_all("span", {"class": "a-offscreen"})
    price = prices[1].text

    if (price == currPrice):
        pass
    elif (price != currPrice):
        print('CHANGED')
        title = "YOUR PRODUCT HAS CHANGED IN PRICE!"
        message = "The product at url " + url + "has changed in price! Check now!"
        notification.notify(title=title, message=message,app_name="Python AmazonTracker" ,app_icon = None, timeout = 500, toast = False, ticker="PRICECHANGE")
        loop = False


    print("Current price: " + price)

    time.sleep(int(minutes)*60)

