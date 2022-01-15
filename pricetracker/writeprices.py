import requests
from datetime import date, datetime
from bs4 import BeautifulSoup as bs

headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}
now = datetime.now()
dtString = now.strftime("%c")

url = "https://www.amazon.com/Aurora-Gaming-Desktop-Geforce-Made_by_Dell/dp/B08N3XZ38B/"
res = requests.get(url, headers=headers)

doc = bs(res.text, "html.parser")

prices = doc.find_all("span", {"class": "a-offscreen"})
prices = prices

f = open("results/" + "PRICE" + dtString + "PRICE", "a")
f.write(str(prices))
f.close()
